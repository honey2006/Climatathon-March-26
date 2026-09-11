import re
import csv


def parse_weather_data(raw_text):
    """
    Parse concatenated dict-like weather records into a list of row dicts.
    Each record looks like:
      {'T2M_MAX': {'20260309': 36.34}, 'T2M_MIN': {'20260309': 21.32}, ...}
    """
    # Find all top-level {...} blocks
    records_raw = re.findall(r'\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}', raw_text)

    rows = []
    for record_str in records_raw:
        # Extract every  'KEY': {'DATE': VALUE}  pair
        pairs = re.findall(r"'(\w+)':\s*\{'(\d{8})':\s*([\d.]+)\}", record_str)
        if not pairs:
            continue

        row = {"DATE": pairs[0][1]}  # grab date from first pair
        for key, date, value in pairs:
            row[key] = float(value)
        rows.append(row)

    return rows


def convert_to_csv(raw_text, output_path):
    rows = parse_weather_data(raw_text)
    if not rows:
        print("No data found. Check input format.")
        return

    all_keys = set()
    for r in rows:
        all_keys.update(r.keys())
    all_keys.discard("DATE")
    fieldnames = ["DATE"] + sorted(all_keys)

    with open(output_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(f"Saved {len(rows)} row(s) to: {output_path}")


def convert_data(INPUT_FILE, OUTPUT_FILE):
    with open(INPUT_FILE) as f:
        raw = f.read()
    convert_to_csv(raw, OUTPUT_FILE)