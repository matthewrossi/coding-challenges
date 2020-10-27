# (0,0) -> (x,y)
# direction up, down, left, right
# i-th jump oves 2^(i-1) (first jump moves 1)
# as short as possible

tests = int(input())
for test in range(1, tests + 1):
    x, y = map(int, input().split())

    x_neg = (x < 0)
    if x < 0:
        x = -x
    y_neg = (y < 0)
    if y < 0:
        y = -y

    path = []
    curr_x = curr_y = 0
    i = 0

    if x & 2**i and not y & 2**i:
        if not x_neg:
            path.append('E')
        else:
            path.append('W')
        x_i += 1
    elif not x & 2**i and y & 2**i:
        if not x_neg:
            path.append('N')
        else:
            path.append('S')
        y_i += 1
    elif x & 2**i and y & 2**i:
        # decide which one to advance
        
    else:
        print("Case #{}: {}".format(test, "IMPOSSIBLE"))
    
    print("Case #{}: {}".format(test, "".join(path)))
