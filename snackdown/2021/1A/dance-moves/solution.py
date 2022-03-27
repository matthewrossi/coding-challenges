#!/usr/bin/env python3

nof_tests = int(input())
for test in range(nof_tests):
    me, partner = map(int, input().split())
    distance = partner - me
    if distance <= 0:
        print(-distance)
    else:
        if distance % 2 == 0:
            print(distance // 2)
        else:
            print(distance // 2 + 2)
