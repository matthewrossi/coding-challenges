t = int(input())
for test in range(1, t + 1):
    n, c = map(int, input().split())

    original = c

    if c < n - 1 or c > (n + 1) * n / 2 - 1:
        print("Case #{}: {}".format(test, "IMPOSSIBLE"))
        continue

    i, j = 0, n - 1
    arr = [None] * n
    to_left = True
    while i <= j:
        num = i + (n - j - 1) + 1
        if c > (n - (num - 1)) * (n - (num - 1) - 1) / 2:
            to_left = not to_left
            if to_left:
                arr[i] = num
                i += 1
            else:
                arr[j] = num
                j -= 1
            c -= n - (num - 1)
        else:
            if to_left:
                arr[i] = num
                i += 1
            else:
                arr[j] = num
                j -= 1
            c -= 1


    print("Case #{}: {}".format(test, " ".join(map(str, arr))))
