#!/bin/python3

import sys

def solve(grades):
    # Complete this function
    res = []
    for grade in grades:
        if (grade < 38) or (grade %5 < 3):
            val = grade
        else:
            grade = grade + (5-(grade%5))
            val = grade
        res.append(val)
    return res
n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))


