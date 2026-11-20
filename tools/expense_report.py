"""CSV 欄位 date,category,amount；金額以十進位處理，統計同一幣別的支出。"""
import argparse
import csv
from datetime import date
from decimal import Decimal, InvalidOperation
from pathlib import Path


def summarize(stream):
    reader = csv.DictReader(stream)
    if reader.fieldnames != ['date', 'category', 'amount']:
        raise ValueError('expected header: date,category,amount')
    totals = {}
    for line, row in enumerate(reader, 2):
        try:
            date.fromisoformat(row['date'])
            category = row['category'].strip()
            amount = Decimal(row['amount'])
            if None in row or not category or not amount.is_finite() or amount < 0 or amount != amount.quantize(Decimal('.01')):
                raise ValueError('invalid category or amount')
        except (ValueError, TypeError, AttributeError, InvalidOperation) as exc:
            raise ValueError(f'invalid expense on line {line}') from exc
        totals[category] = totals.get(category, Decimal(0)) + amount
    return dict(sorted(totals.items()))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('file', type=Path)
    args = parser.parse_args()
    with args.file.open(encoding='utf-8-sig', newline='') as stream:
        totals = summarize(stream)
    for category, amount in totals.items(): print(f'{category}\t{amount:.2f}')
    print(f'TOTAL\t{sum(totals.values(), Decimal(0)):.2f}')


if __name__ == '__main__': main()
