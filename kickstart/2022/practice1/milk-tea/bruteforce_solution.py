def bruteforce(counts):
    complaints = [0] * 2**p
    for i in range(2**p):
        # Avoid inner loop by reusing previous computations
        for j in range(p):
            if (i >> j) % 2:
                complaints[i] += n - counts[p-j-1]
            else:
                complaints[i] += counts[p-j-1]
    return complaints


def solve(prefs, forbiddens):
    n = len(prefs)
    p = len(prefs[0])

    counts = [0] * p
    for i in range(n):
        for j in range(p):
            counts[j] += int(prefs[i][j])

    complaints = bruteforce(counts)
    ids = sorted(list(range(2**p)), key=lambda id: complaints[id])
    for i in ids:
        if i not in forbiddens:
            break

    print(f"{complaints=}")
    print(f"{ids=}")
    print(f"{i=}")
    return complaints[i]


if __name__ == "__main__":
    nof_tests = int(input())
    for test in range(1, nof_tests + 1):
        n, m, p = map(int, input().split())
        prefs = [input() for _ in range(n)]
        forbiddens = {int(input(), base=2) for _ in range(m)}
        res = solve(prefs, forbiddens)
        print("Case #{}: {}".format(test, res))
    