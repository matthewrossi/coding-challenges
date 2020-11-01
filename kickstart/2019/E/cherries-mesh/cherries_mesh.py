def find(x):
    if forest[x] == x:
        return x
    else:
        forest[x] = find(forest[x])
        return forest[x]

def merge(x, y):
    x = find(x)
    y = find(y)
    if (x == y):
        return False
    forest[x] = y
    return True

nof_tests = int(input())
for test in range(1, nof_tests + 1):
    nof_cherries, nof_black = map(int, input().split())
    forest = list(range(nof_cherries + 1))
    weight = 2 * (nof_cherries - 1)
    for i in range(nof_black):
        c, d = map(int, input().split())
        if merge(c, d):
            weight -= 1
    
    print("Case #{}: {}".format(test, weight))
