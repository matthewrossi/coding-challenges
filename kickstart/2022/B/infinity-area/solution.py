#!/usr/bin/env python3

import math

nof_tests = int(input())
for test in range(1, nof_tests + 1):
    r, a, b = map(int, input().split())

    area = r * r
    curr_r = r * a
    area += curr_r * curr_r
    curr_r = curr_r // b
    while curr_r:
        area += curr_r * curr_r
        curr_r = curr_r * a
        area += curr_r * curr_r
        curr_r = curr_r // b

    print("Case #{}: {}".format(test, math.pi * area))
