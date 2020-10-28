nof_tests = int(input())
for test in range(1, nof_tests + 1):
    n = int(input())
    patterns = [input() for _ in range(n)]

    result = patterns[0].split('*')
    for pattern in patterns[1:]:
        toks = pattern.split('*')

        prefix = ''
        if result[0] != '' and toks[0] != '':
            if len(result[0]) >= len(toks[0]):
                if result[0].startswith(toks[0]):
                    prefix = result[0]
                else:
                    print("Case #{}: *".format(test))
                    break
            else:
                if toks[0].startswith(result[0]):
                    prefix = toks[0]
                else:
                    print("Case #{}: *".format(test))
                    break
        else:
            if result[0] != '':
                prefix = result[0]
            if toks[0] != '':
                prefix = toks[0]

        middle = result[1:-1] + toks[1:-1]

        suffix = ''
        if result[-1] != '' and toks[-1] != '':
            if len(result[-1]) >= len(toks[-1]):
                if result[-1].endswith(toks[-1]):
                    suffix = result[-1]
                else:
                    print("Case #{}: *".format(test))
                    break
            else:
                if toks[-1].endswith(result[-1]):
                    suffix = toks[-1]
                else:
                    print("Case #{}: *".format(test))
                    break
        else:
            if result[-1] != '':
                suffix = result[-1]
            if toks[-1] != '':
                suffix = toks[-1]

        result = [prefix]
        result.extend(middle)
        result.append(suffix)
       
    else:
        print("Case #{}: {} ".format(test, "".join(result)))