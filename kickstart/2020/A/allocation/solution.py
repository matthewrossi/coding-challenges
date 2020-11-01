t = int(input())
for test in range(1, t + 1):
    n, b = map(int, input().split()) 
    costs = list(map(int, input().split()))
    costs.sort()
    i = 0
    while i < n and costs[i] <= b:
        b -= costs[i]
        i += 1
    print("Case #{}: {}".format(test, i))
