#!/usr/bin/env python3

import sys

current_district = None
total = 0.0

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    district, expenditure = line.split("\t")

    expenditure = float(expenditure)

    if current_district == district:
        total += expenditure
    else:
        if current_district is not None:
            print(f"{current_district}\t{total:.2f}")

        current_district = district
        total = expenditure

if current_district is not None:
    print(f"{current_district}\t{total:.2f}")
