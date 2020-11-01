from bisect import bisect_left

def code_eat_rate(val):
    if val[1]:
        return val[0] / val[1]
    else:
        return 10**5

nof_tests = int(input())
for test in range(1, nof_tests + 1):
    nof_days, nof_slots = map(int, input().split())
    slots = []
    for slot in range(nof_slots):
        code, eat = map(int, input().split())
        slots.append([code, eat])

    slots.sort(key=code_eat_rate)

    code_cum = [0] * (nof_slots)
    eat_cum = [slots[0][1]] * (nof_slots)
    for i in range(1, nof_slots):
        code_cum[i] = code_cum[i - 1] + slots[nof_slots - i][0]
        eat_cum[i] = eat_cum[i - 1] + slots[i][1]

    out = []
    for day in range(nof_days):
        to_code, to_eat = map(int, input().split())
        to_split = bisect_left(eat_cum, to_eat)

        if (to_split < nof_slots):
            factor = (eat_cum[to_split] - to_eat) / slots[to_split][1]
            current_code = code_cum[nof_slots - to_split - 1] + factor * slots[to_split][0]
            if current_code >= to_code:
                out.append("Y")
            else:
                out.append("N")
        else:
            out.append("N")           

    print("Case #{}: {}".format(test, "".join(out)))