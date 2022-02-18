def best_teas(counts, n, m):
    solutions = {"": 0}
    for i in range(p):
        candidates = {}
        # Identify candidate solutions and compute their score
        for tea, nof_complaints in solutions.items():
            for value in [0, 1]:
                new_tea = tea + str(value)
                additional_complaints = n - counts[i] if value else counts[i]
                candidates[new_tea] = nof_complaints + additional_complaints
        # Keep the best performing m + 1 candidates
        teas = sorted(candidates.keys(), key=lambda prefix: candidates[prefix])
        solutions = {}
        for tea in teas[:m + 1]:
            nof_complaints = candidates[tea]
            solutions[tea] = nof_complaints
    return solutions


def solve(prefs, forbiddens):
    n = len(prefs)
    m = len(forbiddens)
    p = len(prefs[0])

    counts = [0] * p
    for i in range(n):
        for j in range(p):
            counts[j] += int(prefs[i][j])

    complaints = best_teas(counts, n, m)
    for tea in complaints:
        if tea not in forbiddens:
            break

    return complaints[tea]


if __name__ == "__main__":
    nof_tests = int(input())
    for test in range(1, nof_tests + 1):
        n, m, p = map(int, input().split())
        prefs = [input() for _ in range(n)]
        forbiddens = {input() for _ in range(m)}
        res = solve(prefs, forbiddens)
        print("Case #{}: {}".format(test, res))
    