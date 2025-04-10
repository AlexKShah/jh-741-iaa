"""
Filename: parsehttplog.py
Author: Alex Shah
Created: 2025-04-10
Description:
    EN.695.741.81.SP25 Information Assurance Analysis
    Mod 10 Splunk Assignment
    
    Parse HTTP log script
    
    Run with uv:
        uv run --with pandas parsehttplog.py \
            <filename> <record number> <field1> [<field2 ...] [--verbose]
"""

import sys
import pandas as pd
import re
from datetime import datetime

COLUMNS = ['ip', 'datetime', 'uri', 'response', 'size', 'ref', 'useragent']

SUSPICIOUS = [
    r"<\?system", r"cmd=", r"\.php", r"/admin", r"select\s+\*\s+from",
    r"curl", r"python-requests", r"nmap", r"sqlmap", r"wget"
]

def is_problematic(record):
    issues = []

    if not record['useragent'] or len(record['useragent']) < 5:
        issues.append("useragent too short or missing")

    for pattern in SUSPICIOUS:
        if re.search(pattern, record['useragent'], re.IGNORECASE):
            issues.append(f"Suspicious useragent: {pattern}")
        if re.search(pattern, record['uri'], re.IGNORECASE):
            issues.append(f"Suspicious uri: {pattern}")

    return issues

def parse_datetime(date_str):
    try:
        return datetime.strptime(date_str, '%d/%b/%Y:%H:%M:%S %z')
    except ValueError:
        return None

def parse_log_file(filepath, verbose=False):
    valid_records = []
    corrupt_few, corrupt_many, problems = 0, 0, 0
    problematic_lines = []

    with open(filepath, encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            parts = line.strip().split('|')

            if len(parts) < 7:
                corrupt_few += 1
                if verbose:
                    print(f"[Too Few Fields] Line {line_num}: {line.strip()}")
                continue
            if len(parts) > 7:
                corrupt_many += 1
                if verbose:
                    print(f"[Too Many Fields] Line {line_num}: {line.strip()}")
                continue

            try:
                datetime_value = parse_datetime(parts[1])
                if datetime_value is None:
                    raise ValueError("Invalid datetime format")

                record = {
                    'ip': parts[0],  # ip as string
                    'datetime': datetime_value,  # datetime
                    'uri': parts[2],  # uri as string
                    'response': int(parts[3]),  # response as int
                    'size': int(parts[4]),  # size as int
                    'ref': parts[5],  # referrer as string
                    'useragent': parts[6]  # useragent as string
                }
            except ValueError as e:
                problems += 1
                problematic_lines.append((line_num, str(e)))
                continue

            record['record_number'] = line_num

            issues = is_problematic(record)
            if issues:
                problems += 1
                problematic_lines.append((line_num, ' '.join(issues)))
                continue

            valid_records.append(record)

    if valid_records:
        df = pd.DataFrame(valid_records)
        df['record_number'] = df['record_number'].astype(int)
        df.set_index('record_number', inplace=True)
    else:
        df = pd.DataFrame(columns=COLUMNS)
    
    #DEBUG
    if verbose:
        print(f"\nParsed {len(df)} valid records")
        print(f"Corrupt (too few fields): {corrupt_few}")
        print(f"Corrupt (too many fields): {corrupt_many}")
        print(f"Problematic records: {problems}")
        print("\nProblematic Lines:")
        for line_num, reason in problematic_lines:
            print(f"Line {line_num}: {reason}")
    
    return df, corrupt_few, corrupt_many, problems

def show_record(df, record_num, fields):
    if record_num not in df.index:
        print(f"Record {record_num} not found (corrupt or filtered).")
        return

    print(f"\nRecord {record_num}:")
    for field in fields:
        if field in df.columns:
            print(f"{field}: {df.at[record_num, field]}")

def main():
    verbose = '--verbose' in sys.argv
    filepath = sys.argv[1]
    record_num = int(sys.argv[2])
    fields = sys.argv[3:]

    df, corrupt_few, corrupt_many, problems = parse_log_file(filepath, verbose)
    show_record(df, record_num, fields)

    print(f"\nSummary:")
    print(f"Valid records: {len(df)}")
    print(f"Invalid records: {corrupt_few + corrupt_many + problems}")

if __name__ == "__main__":
    main()
