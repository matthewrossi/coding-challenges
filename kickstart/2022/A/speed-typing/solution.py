nof_tests = int(input())
for test in range(1, nof_tests + 1):
    to_write = input()
    written = input()

    budget = len(written) - len(to_write)

    is_impossible = False if budget >= 0 else True
    deleted = 0
    for i, target in enumerate(to_write):
        while deleted < budget and target != written[i + deleted]:
            deleted += 1
        if deleted == budget and target != written[i + deleted]:
            is_impossible = True
            break;

    solution = "IMPOSSIBLE" if is_impossible else budget
    print("Case #{}: {}".format(test, solution))
