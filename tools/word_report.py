"""python -m tools.word_report notes.txt --top 10；以連續英數字元或中文字組為詞。"""
import argparse
from collections import Counter
from pathlib import Path
import re


def frequent_words(text, limit=10):
    if limit < 1: raise ValueError('limit must be positive')
    counts = Counter(re.findall(r'[^\W_]+', text.casefold(), flags=re.UNICODE))
    return sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:limit]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('file', type=Path)
    parser.add_argument('--top', type=int, default=10)
    args = parser.parse_args()
    for word, count in frequent_words(args.file.read_text(encoding='utf-8-sig'), args.top):
        print(f'{word}\t{count}')


if __name__ == '__main__': main()
