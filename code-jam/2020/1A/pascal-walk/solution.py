# given a pascal triangle find a sequence (<= 500) 
# such that the sum of the numbers is equal to N

def walk(level, i, n):
    if n == 0:
        return

    result.append((level + 1, i + 1))
    n -= pascal[level][i]

    mid = (level + 1) / 2
    if i <= mid:
        cost = sum(pascal[level + 1][:i + 1])
        if i == 0 or n > cost:
            walk(level + 1, i, n)
        else:
            walk(level, i - 1, n)
    else:
        cost = sum(pascal[level + 1][i + 1:])
        if i == level or n > cost:
            walk(level + 1, i + 1, n)
        else:
            walk(level, i + 1, n)

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

nof_tests = int(input())
for test in range(1, nof_tests + 1):
    ver = n = tmp = int(input())

    level = 0
    while tmp:
        tmp >>= 1
        level += 1
    level -= 1

    result = []
    for l in range(1, level + 1):
        if not l % 2:
            result.extend([(l, i) for i in range(1, l + 1)])
        else:
            result.extend([(l, i) for i in range(l, 0, -1)])
    n -= 2**level - 1

    if level % 2:
        i = min = 0
        mid = (level + 1) / 2
        while n > pascal[level][i] + pascal[level + 1][i] + min:
            result.append((level + 1, i + 1))
            n -= pascal[level][i]
            i += 1
            if i < mid:
                min += pascal[level + 1][i]
            else:
                min -= pascal[level + 1][i + 1]
        if i:
            result.pop()
            i -= 1
            n += pascal[level][i]
        walk(level, i, n)

    else:
        i = level
        min = 0
        mid = int((level + 1) / 2)
        while n > pascal[level][i] + pascal[level + 1][i + 1] + min:
            result.append((level + 1, i + 1))
            n -= pascal[level][i]
            i -= 1
            if i >= mid:
                min += pascal[level + 1][i + 1]
            else:
                min -= pascal[level + 1][i]
        if i != level:
            result.pop()
            i += 1
            n += pascal[level][i]
        walk(level, i, n)

    # tot = 0
    # for l, i in result:
    #     tot += pascal[l - 1][i - 1]
    # assert tot == ver

    print("Case #{}:".format(test))
    for l, i in result:
        print(l, i)
