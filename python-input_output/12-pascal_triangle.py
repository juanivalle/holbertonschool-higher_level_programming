#!/usr/bin/python3
"""comments"""


def pascal_triangle(n):
    triangle = []
    row = []
    pre = []
    for i in range(0, n + 1):
        row = [j > 0 and j < i - 1 and i > 2 and pre[j-1] + pre[j] or 1 for j in range(0, i)]
        pre = row
        triangle += [row]
    return triangle[1:]
