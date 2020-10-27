nof_tests = int(input())
for test in range(1, nof_tests + 1):
    n = int(input())

    result = []
    if n > 30:
        tmp = n - 30
        level = 1
        empty = 0
        while tmp:
            b = tmp % 2
            if b:
                if result and result[-1][1] == 1:
                    result.extend([(level, i) for i in range(1, level + 1)])
                else:
                    result.extend([(level, i) for i in range(level, 0, -1)])
            else:
                result.append((level, 1 if result and result[-1][1] == 1 else level))
                empty += 1
            level += 1
            tmp >>= 1
        
        if result and result[-1][1] == 1:
            result.extend([(level + i, 1) for i in range(30 - empty)])
        else:
            result.extend([(level + i, level + i) for i in range(30 - empty)])
    else:
        result.extend(enumerate([1] * n, 1))

    print("Case #{}:".format(test))
    for l, i in result:
        print(l, i)
