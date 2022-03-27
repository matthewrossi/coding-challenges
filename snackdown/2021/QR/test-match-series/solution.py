#!/usr/bin/env python3

nof_tests = int(input())
for test in range(1, nof_tests + 1):
    results = list(map(int, input().split()))

    win_count = lose_count = 0
    for result in results:
        if result == 1:
            win_count += 1
        elif result == 2:
            lose_count += 1

    if win_count > lose_count:
        print("INDIA")
    elif win_count == lose_count:
        print("DRAW")
    else:
        print("ENGLAND")
