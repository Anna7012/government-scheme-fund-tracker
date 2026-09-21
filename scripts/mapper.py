#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.strip()

    if not line or line.startswith("District,"):
        continue

    parts = line.split(",")

    if len(parts) != 3:
        continue

    district = parts[0]
    expenditure = parts[2]

    print(f"{district}\t{expenditure}")
