nof_tests = int(input())
for test in range(1, nof_tests + 1):
    nesting = 0
    result = []
    for ch in input():
        delta = int(ch) - nesting
        if delta > 0:
            for _ in range(delta):
                result.append("(")
            nesting = int(ch)
        elif delta < 0:
            for _ in range(-delta):
                result.append(")")
            nesting = int(ch)
        result.append(ch)

    for _ in range(nesting):
        result.append(")")

    print("Case #{}: {}".format(test, ''.join(result)))