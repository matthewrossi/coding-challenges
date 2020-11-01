t = int(input())
for test in range(1, t + 1):
    n = int(input())
    m = [list(map(int, input().split())) for _ in range(n)]

    result = 0
    for i in range(n):
        current = j = 0
        while (i + j < n):
            current += m[i + j][j]
            j += 1
        result = max(result, current)
    
    m = list(map(list, zip(*m)))

    for i in range(n):
        current = j = 0
        while (i + j < n):
            current += m[i + j][j]
            j += 1
        result = max(result, current)

    print("Case #{}: {}".format(test, result))
