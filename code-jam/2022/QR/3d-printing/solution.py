NOF_PRINTERS = 3
INK_COST_PER_PRINTER = 10**6

nof_test = int(input())
for test in range(1, nof_test + 1):
    printers = [list(map(int, input().split())) for _ in range(NOF_PRINTERS)]

    colors = zip(*printers)
    limits = list(map(min, colors))

    total = INK_COST_PER_PRINTER
    color = [0] * len(limits)
    for i, limit in enumerate(limits):
        color[i] = min(total, limit)
        total -= color[i]
    solution = "IMPOSSIBLE" if total else " ".join(map(str, color))

    print("Case #{}: {}".format(test, solution))
