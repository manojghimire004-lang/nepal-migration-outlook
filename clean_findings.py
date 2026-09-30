"""Clean and validate an aggregate findings CSV; never infer respondent records."""
import argparse
import csv
from decimal import Decimal, InvalidOperation
from pathlib import Path

NUMERIC = ('Count', 'Denominator', 'Percentage', 'Mean_1_to_5')

def clean(source, destination):
    with Path(source).open(encoding='utf-8-sig', newline='') as handle:
        reader = csv.DictReader(handle)
        headers = reader.fieldnames
        required = {'Section', 'Finding', 'Scope', *NUMERIC}
        if not headers or not required.issubset(headers):
            raise ValueError('Input is missing required findings columns')
        rows, seen = [], set()
        duplicates = 0
        for line, raw in enumerate(reader, 2):
            if None in raw or any(value is None for value in raw.values()):
                raise ValueError(f'Row {line}: unexpected number of fields')
            row = {key: value.strip() for key, value in raw.items()}
            for key in NUMERIC:
                if not row[key]:
                    continue  # Unavailable values stay blank, not zero.
                try:
                    number = Decimal(row[key])
                except InvalidOperation as error:
                    raise ValueError(f'Row {line}: invalid {key}') from error
                if not number.is_finite() or number < 0:
                    raise ValueError(f'Row {line}: invalid {key}')
                if key in ('Count', 'Denominator') and number != number.to_integral_value():
                    raise ValueError(f'Row {line}: {key} must be an integer')
                if key == 'Percentage' and number > 100:
                    raise ValueError(f'Row {line}: percentage exceeds 100')
                if key == 'Mean_1_to_5' and not 1 <= number <= 5:
                    raise ValueError(f'Row {line}: mean outside 1–5')
                row[key] = format(number, 'f')
            if row['Count'] and row['Denominator']:
                count, denominator = Decimal(row['Count']), Decimal(row['Denominator'])
                if denominator == 0 or count > denominator:
                    raise ValueError(f'Row {line}: invalid count/denominator')
                if row['Percentage'] and abs(Decimal(row['Percentage']) - count / denominator * 100) > Decimal('0.11'):
                    raise ValueError(f'Row {line}: percentage does not reconcile')
            signature = tuple(row[key] for key in headers)
            if signature in seen:
                duplicates += 1
                continue
            seen.add(signature)
            rows.append(row)
    destination = Path(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open('w', encoding='utf-8', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)
    return {'rows_written': len(rows), 'duplicate_rows_removed': duplicates}

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', default='survey_findings_source.csv')
    parser.add_argument('--output', default='survey_findings_clean.csv')
    args = parser.parse_args()
    print(clean(args.input, args.output))
