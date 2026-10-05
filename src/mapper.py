#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.strip()

    if not line or line.startswith("Student_ID"):
        continue

    fields = line.split(",")

    department = fields[2]
    marks = fields[5]

    print(f"{department}\t{marks}")