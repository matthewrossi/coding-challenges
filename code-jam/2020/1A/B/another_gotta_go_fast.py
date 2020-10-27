pascal = []
for r in range(500):
    current = [0] * (r + 1)
    for k in range(r + 1):
        if k == 0 or k == r:
            current[k] = 1
        else:    
            prev = pascal[r - 1]
            current[k] = prev[k - 1] + prev[k]
    pascal.append(current)
#print(*pascal[:10], sep="\n")

nof_tests = int(input())
for test in range(1, nof_tests + 1):
    n = int(input())

    result = []
    tot = level = pos = 0
    # zig-zag
    to_side = sum(pascal[level][:pos + 1])
    while tot + to_side <= n:
        result.append((level + 1, pos + 1))
        tot += pascal[level][pos]
        level += 1

        if not level % 2:
            pos += 1
        to_side = sum(pascal[level][:pos + 1])

    pos -= 1        # undo last increment in position
    if level % 2:
        level -= 1  # undo last increment in level
    elif not level % 2 and tot + (to_side - pascal[level][pos + 1]) > n:
        level -= 1  # undo last increment in level
        pos -= 1    # avoid repeating the element

    # keep position / go left
    while tot < n:
        result.append((level + 1, pos + 1))
        tot += pascal[level][pos]
        if tot + sum(pascal[level + 1][:pos + 1]) <= n:
            level += 1
        else:
            pos -= 1

    """tot = 0
    for l, i in result:
        tot += pascal[l - 1][i - 1]
    print(f"n = {n}, tot = {tot}")"""

    print("Case #{}:".format(test))
    for l, i in result:
        print(l, i)
