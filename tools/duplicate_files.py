"""唯讀重複檔案報告：先依大小分組，再以 SHA256 比對內容；跳過符號連結。"""
import argparse
from collections import defaultdict
import hashlib
from pathlib import Path


def find_duplicates(root):
    root = Path(root)
    if not root.is_dir(): raise ValueError('root must be a directory')
    sizes = defaultdict(list)
    for path in sorted(root.rglob('*')):
        if not path.is_symlink() and path.is_file():
            sizes[path.stat().st_size].append(path)
    matches = []
    for candidates in sizes.values():
        if len(candidates) < 2: continue
        hashes = defaultdict(list)
        for path in candidates:
            digest = hashlib.sha256()
            with path.open('rb') as stream:
                for chunk in iter(lambda: stream.read(65536), b''): digest.update(chunk)
            hashes[digest.hexdigest()].append(path)
        matches.extend(group for group in hashes.values() if len(group) > 1)
    return sorted(matches, key=lambda group: str(group[0]))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('directory', type=Path)
    root = parser.parse_args().directory
    for group in find_duplicates(root):
        print('\n'.join(str(path) for path in group)); print()
