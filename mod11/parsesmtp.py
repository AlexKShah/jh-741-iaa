import re
import pandas as pd
from collections import defaultdict
from typing import List, Dict

LOG_FIELDS = ['timestamp', 'log_level', 'message']

def read_log_file(filename: str) -> pd.DataFrame:
    with open(filename, 'r') as f:
        lines = f.readlines()

    data = []
    for line in lines:
        parts = line.strip().split(' ', 4)
        if len(parts) == 5:
            timestamp = ' '.join(parts[:3])
            log_level = parts[3]
            message = parts[4]
            data.append([timestamp, log_level, message])
    return pd.DataFrame(data, columns=LOG_FIELDS)

def extract_ids(df: pd.DataFrame) -> pd.DataFrame:
    df['MID'] = df['message'].str.extract(r'MID (\d+)')
    df['ICID'] = df['message'].str.extract(r'ICID (\d+)')
    df['IP'] = df['message'].str.extract(r'address ([\d.]+)')
    df['From'] = df['message'].str.extract(r'From: <([^>]+)>')
    df['To'] = df['message'].str.extract(r'To: <([^>]+)>')
    return df

def build_mappings(df: pd.DataFrame):
    # Maps ICID to IP
    icid_to_ip = df.dropna(subset=['ICID', 'IP']).set_index('ICID')['IP'].to_dict()

    # Maps MID to ICID
    mid_to_icid = df.dropna(subset=['MID', 'ICID']).set_index('MID')['ICID'].to_dict()

    # Maps MID to From and To
    mid_to_from = df.dropna(subset=['MID', 'From']).set_index('MID')['From'].to_dict()
    mid_to_to = df.dropna(subset=['MID', 'To']).set_index('MID')['To'].to_dict()

    return icid_to_ip, mid_to_icid, mid_to_from, mid_to_to

def get_unique_emails_and_domains(emails: List[str]) -> (set, set):
    email_set = set(filter(None, emails))
    domain_set = set(email.split('@')[1] for email in email_set if '@' in email)
    return email_set, domain_set

def filter_mids(df: pd.DataFrame, condition: str) -> List[str]:
    grouped = df.groupby('MID')['message'].apply(lambda x: ' '.join(x.dropna()))
    if condition == 'spam_positive':
        return grouped[grouped.str.contains('CASE spam positive', case=False)].index.tolist()
    elif condition == 'antivirus_positive':
        return grouped[grouped.str.contains('antivirus positive', case=False)].index.tolist()
    elif condition == 'not_done':
        return grouped[~grouped.str.contains('done', case=False)].index.tolist()
    elif condition == 'not_queued':
        return grouped[~grouped.str.contains('queued for delivery', case=False)].index.tolist()
    else:
        return []

def correlate_ips_to_mids(df: pd.DataFrame, icid_to_ip: Dict[str, str], mid_to_icid: Dict[str, str]) -> pd.DataFrame:
    df_mid = df[df['MID'].notna()].copy()
    df_mid['IP'] = df_mid['ICID'].map(icid_to_ip)
    return df_mid

def analyze_spam_ips(df: pd.DataFrame) -> pd.DataFrame:
    spam_mids = filter_mids(df, 'spam_positive')
    icid_to_ip, mid_to_icid, mid_to_from, mid_to_to = build_mappings(df)
    df_correlated = correlate_ips_to_mids(df, icid_to_ip, mid_to_icid)
    spam_df = df_correlated[df_correlated['MID'].isin(spam_mids)]
    return spam_df[['timestamp', 'MID', 'ICID', 'IP', 'From', 'To', 'message']].drop_duplicates()

def summarize_addresses(mid_to_from: Dict[str, str], mid_to_to: Dict[str, str]):
    from_emails, from_domains = get_unique_emails_and_domains(list(mid_to_from.values()))
    to_emails, to_domains = get_unique_emails_and_domains(list(mid_to_to.values()))

    print(f"\nUnique From Addresses ({len(from_emails)}): {from_emails}")
    print(f"Unique From Domains ({len(from_domains)}): {from_domains}")
    print(f"Unique To Addresses ({len(to_emails)}): {to_emails}")
    print(f"Unique To Domains ({len(to_domains)}): {to_domains}")

def display_filtered(df: pd.DataFrame, condition: str):
    mids = filter_mids(df, condition)
    print(f"\nCondition '{condition}' matched {len(mids)} MIDs\n")
    filtered_df = df[df['MID'].isin(mids)]
    print(filtered_df[['timestamp', 'MID', 'ICID', 'IP', 'From', 'To', 'message']].drop_duplicates())

def main(filename: str):
    df = read_log_file(filename)
    df = extract_ids(df)
    icid_to_ip, mid_to_icid, mid_to_from, mid_to_to = build_mappings(df)

    # Run filters
    for condition in ['spam_positive', 'antivirus_positive', 'not_done', 'not_queued']:
        display_filtered(df, condition)

    # Spam IP analysis
    spam_df = analyze_spam_ips(df)
    print("\n== IPs associated with spam messages ==")
    print(spam_df[['IP', 'From', 'To']].dropna().drop_duplicates())

    summarize_addresses(mid_to_from, mid_to_to)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python smtp_log_analyzer.py <logfile>")
    else:
        main(sys.argv[1])
