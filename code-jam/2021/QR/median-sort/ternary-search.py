import sys

def ask(a, b, c):
    print(a, b, c)
    res = int(input())
    if res == -1: sys.exit()
    return res

t, n, q = map(int, input().split())
for test in range(t):
    # insertion sort
    indexes = [1, 2]
    for i in range(3, n + 1):
        # ternary search where to put i
        start = 0
        end = len(indexes) + 1
        while start + 1 < end:
            first = start + (end - start) // 3
            second = start + 2 * (end - start) // 3

            if first == 0: first += 1
            while second <= first: second += 1
            if second == i: second -= 1
            while first >= second: first -= 1

            median = ask(i, indexes[first - 1], indexes[second - 1])
            if i == median:
                start = max(start, first)
                end = min(end, second)
            elif indexes[first - 1] == median:
                end = min(end, first)
            elif indexes[second - 1] == median:
                start = max(start, second)
        # move i to position
        indexes.append(None)
        for j in range(len(indexes) - 1, start, -1):
            indexes[j] = indexes[j - 1]
        indexes[start] = i

    print(" ".join(map(str, indexes)), flush=True)
    verdict = int(input())
    if verdict == -1: sys.exit()
