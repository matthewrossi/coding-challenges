from collections import defaultdict

t = int(input())
for test in range(1, t + 1):
    w, n = map(int, input().split())
    pos = list(map(int, input().split()))

    done = {}
    for p in pos:
        done[p] = False

    result = float("+inf")
    for target in pos:
        if not done[target]:
            current = 0
            for p in pos:
                if target > p:
                    current += min(target - p, n - target + p)
                else:
                    current += min(p - target, n - p + target)
            if result > current:
                result = current
            done[target] = True

    print("Case #{}: {}".format(test, result))
