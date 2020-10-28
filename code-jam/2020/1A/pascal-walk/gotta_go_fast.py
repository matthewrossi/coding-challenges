def walk(level, pos, tot):
    result = []
    to_side = sum(pascal[level][:pos + 1])
    while tot + to_side <= n:
        result.append((level + 1, pos + 1))
        tot += pascal[level][pos]
        level += 1

        to_side = sum(pascal[level][:pos + 1])
        # move to the right when possible
        if not level % 2 and tot + to_side + pascal[level][pos + 1] <= n:
            to_side += pascal[level][pos + 1]
            pos += 1

    if tot < n:
        result.extend(walk(level - 1, pos - 1 if pos else 0, tot))

    return result

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

    result = walk(0, 0, 0)

    """tot = 0
    for l, i in result:
        tot += pascal[l - 1][i - 1]
    print(f"n = {n}, tot = {tot}")"""
    
    print("Case #{}:".format(test))
    for l, i in result:
        print(l, i)
