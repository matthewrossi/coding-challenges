nof_test = int(input())
for test in range(1, nof_test + 1):
    n = int(input())
    dices = list(map(int, input().split()))

    dices.sort()
    i = 0
    for nof_sides in dices:
        if nof_sides > i:
            i += 1

    print("Case #{}: {}".format(test, i))
