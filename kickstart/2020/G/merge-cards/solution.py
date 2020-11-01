import math

t = int(input())
for test in range(1, t + 1):
    n = int(input())
    values = list(map(int, input().split()))

    result = 0
    cases = 0
    stack = [(values)]
    while(stack):
        values = stack.pop()

        for i in range(len(values) - 1):
            points = values[i] + values[i + 1]
            tail = values[i + 2:] if i + 2 < n else []
            output = values[:i] + [points] + tail
            stack.append(output)
            result += points / len(output) - 1

    print("Case #{}: {}".format(test, "{:.6f}".format(result)))
