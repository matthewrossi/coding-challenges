#!/usr/bin/env python3

MODULO = 10**9 +7

def main():
    n, m = map(int, input().split())
    jobs = map(int, input().split())

    res = 0
    if m == 1:
        res = 0
        for job in jobs:
            res = (res + (2**job) % MODULO) % MODULO
    else:
        res = 2**max(jobs) % MODULO
    print(res)


if __name__ == "__main__":
    main()