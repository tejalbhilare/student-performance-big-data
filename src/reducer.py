#!/usr/bin/env python3

import sys

current_department = None
total_marks = 0
student_count = 0

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    department, marks = line.split("\t")

    marks = float(marks)

    if current_department == department:
        total_marks += marks
        student_count += 1
    else:
        if current_department is not None:
            average = total_marks / student_count
            print(f"{current_department}\t{average:.2f}")

        current_department = department
        total_marks = marks
        student_count = 1

if current_department is not None:
    average = total_marks / student_count
    print(f"{current_department}\t{average:.2f}")