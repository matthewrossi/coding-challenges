t = int(input())
for test in range(1, t + 1):
    n = int(input())
    visitors = list(map(int, input().split()))
    prev_max = -1
    result = 0
    for i in range(len(visitors)):
        if prev_max < visitors[i]:
            if i + 1 >= n or visitors[i] > visitors[i + 1]:
                result += 1
            prev_max = visitors[i]
    print("Case #{}: {}".format(test, result))
