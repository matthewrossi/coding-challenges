tests = int(input())
for test in range(1, tests + 1):
    x, y, moves = input().split()
    x, y = int(x), int(y)
    
    i = 0
    for char in moves:
        if char == 'N':
            y += 1
        elif char == 'E':
            x += 1
        elif char == 'S':
            y -= 1
        elif char == 'W':    
            x -= 1
        i += 1
        if abs(x) + abs(y) <= i:
            print("Case #{}: {}".format(test, i))   
            break
    else:     
        print("Case #{}: {}".format(test, "IMPOSSIBLE"))
