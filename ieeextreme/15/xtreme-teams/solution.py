import itertools
from collections import defaultdict
from math import comb


t = int(input())

for i in range(t):
    n, m = [int(x) for x in input().split(" ")]
    studs = defaultdict(int)
    for j in range(n):
        studs[input()] += 1
    
    res = 0
    for k in range(1, 4):
        all_poss = itertools.combinations(studs.keys(), k)
        for poss in all_poss:
            team_size = 0
            for elem in poss:
                team_size += studs[elem]

            if team_size >= 3:
                check = [False for i in range(m)]
                for elem in poss:
                    for j in range(m):
                        if elem[j] == "y":
                            check[j] = True
                if all(check):
                    if k == 1:
                        current_result = comb(team_size, 3)
                    elif k == 2:
                        current_result = 0
                        if studs[poss[0]] > 1:
                            current_result += comb(studs[poss[0]], 2) * studs[poss[1]]
                        if studs[poss[1]] > 1:
                            current_result += comb(studs[poss[1]], 2) * studs[poss[0]]
                    elif k == 3:
                        current_result = 1
                        for elem in poss:
                            current_result *= studs[elem]
                    res += current_result
    print(res)
