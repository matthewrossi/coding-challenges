nof_test = int(input())
for test in range(1, nof_test + 1):
    n = int(input())
    values = list(map(int, input().split()))
    nexts = list(map(int, input().split()))

    min_at = [None] * (n + 1)

    tot = 0
    for current in range(n - 1, -1, -1):
        if min_at[current + 1] is not None:
            values[current] = max(values[current], min_at[current + 1])
        next = nexts[current]

        if min_at[next] is None:
            min_at[next] = values[current]
            continue

        if values[current] < min_at[next]:
            tot += min_at[next]
            min_at[next] = values[current]
        else:
            tot += values[current]

    print("Case #{}: {}".format(test, tot + min_at[0]))
