#!/usr/bin/python3
"""Python program to handle Pascal Triangle."""


def pascal_triangle(n):
    """Create function def pascal_triangle(n): that returns list of lists
    of integers representing the Pascal triangle of n
    """
    if n <= 0:
        return []
    res = [[1]]
    for i in range(n - 1):
        s = [1]
        for j in range(i):
            s.append(res[i][j]+res[i][j+1])
        s.append(1)
        res.append(s)
    return res
