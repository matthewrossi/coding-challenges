t = int(input())
for test in range(1, t + 1):
    n, k = map(int, input().split()) 
    a = list(map(int, input().split()))

    i = answer = 0
    in_count_down = False
    while i < n:
        if in_count_down and a[i] != a[i - 1] - 1:
            in_count_down = False
        if in_count_down and a[i] == 1:
            answer += 1
        if a[i] == k:
            in_count_down = True
        i += 1

    print("Case #{}: {}".format(test, answer))
