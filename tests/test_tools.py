import io
from pathlib import Path
from decimal import Decimal
import tempfile
import unittest
from tools.word_report import frequent_words
from tools.expense_report import summarize
from tools.duplicate_files import find_duplicates


class ToolTests(unittest.TestCase):
    def test_words(self):
        self.assertEqual(frequent_words('Hello hello WORLD 世界 世界 _', 2), [('hello', 2), ('世界', 2)])
        self.assertEqual(frequent_words('!!!'), [])

    def test_decimal_csv_and_quoted_category(self):
        data = 'date,category,amount\n2026-01-01,"food,drink",0.10\n2026-01-02,"food,drink",0.20\n'
        self.assertEqual(summarize(io.StringIO(data)), {'food,drink': Decimal('.30')})

    def test_bad_expenses(self):
        for row in ('2026-02-30,food,1', '2026-01-01,food,NaN', '2026-01-01,food,-1', '2026-01-01,food,1.001', '2026-01-01,food,2,extra', '2026-01-01,food'):
            with self.subTest(row=row), self.assertRaises(ValueError):
                summarize(io.StringIO('date,category,amount\n' + row))

    def test_duplicates_are_read_only(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            contents = {'a.bin': b'abc', 'b.bin': b'abc', 'c.bin': b'abd', 'empty1': b'', 'empty2': b''}
            for name, data in contents.items(): (root / name).write_bytes(data)
            groups = {frozenset(path.name for path in group) for group in find_duplicates(root)}
            self.assertEqual(groups, {frozenset(('a.bin', 'b.bin')), frozenset(('empty1', 'empty2'))})
            self.assertEqual({p.name: p.read_bytes() for p in root.iterdir()}, contents)


if __name__ == '__main__': unittest.main()
