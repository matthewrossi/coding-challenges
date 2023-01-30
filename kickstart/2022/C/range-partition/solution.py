#!/usr/bin/env python3

def partition(n, partition_sum):
    assert(n >= 0 and partition_sum >= 0)
    if n == 0 or partition_sum == 0:
        return []
    if n > partition_sum:
        return partition(n - 1, partition_sum)
    else:
        return [n] + partition(n - 1, partition_sum - n)


nof_tests = int(input())
for test in range(1, nof_tests + 1):
    n, x, y = map(int, input().split())

    total_sum = n * (n + 1) // 2
    if total_sum % (x + y):
        print("Case #{}: {}".format(test, "IMPOSSIBLE"))
        continue

    # times = total_sum // (x + y)
    # partition_sum = x * times
    # numbers = partition(n, a)

    numbers = []

    times = total_sum // (x + y)
    partition_sum = x * times

    while n and partition_sum:
        if partition_sum >= n:
            partition_sum -= n
            numbers.append(n)
        n -= 1
   
    print("Case #{}: {}".format(test, "POSSIBLE"))
    print(len(numbers))
    print(" ".join(map(str, numbers)))
