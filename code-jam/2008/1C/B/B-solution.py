mod = 2 * 3 * 5 * 7

nof_cases = int(input())
for case in range(1, nof_cases+1):
    string = input()
    dyn = [[0 for j in range(mod)] for i in range(41)]
    dyn[0][0] = 1
    for i in range(len(string)):                        # picks where to put the sign
        for sgn in range(1 if i == 0 else -1, 2, 2):    # picks the sign
            cur = 0
            for j in range(i, len(string)):             # picks the following number
                cur = (cur * 10 + int(string[j]) - int('0')) % mod
                for x in range(mod):
                    dyn[j+1][(x+sgn * cur+mod) % mod] += dyn[i][x]
    ret = 0
    for x in range(mod):
        if x % 2 == 0 or x % 3 == 0 or x % 5 == 0 or x % 7 == 0:
            ret += dyn[len(string)][x]
    print("Case #{}: {}".format(case, ret))
