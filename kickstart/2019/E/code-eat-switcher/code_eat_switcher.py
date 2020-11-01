def code_eat_rate(val):
    if val[1]:
        return val[0] / val[1]
    else:
        return 10**5


nof_tests = int(input())
for test in range(1, nof_tests + 1):
    nof_days, nof_slots = map(int, input().split())
    slots = []
    max_code = max_eat = 0
    for slot in range(nof_slots):
        code, eat = map(int, input().split())
        slots.append([code, eat])
        max_code += code
        max_eat += eat

    slots.sort(key=code_eat_rate)
    out = []
    for day in range(nof_days):
        to_code, to_eat = map(int, input().split())
        if to_code > max_code or to_eat > max_eat:
            out.append("N")
            continue
        
        current_code = max_code
        current_eat = 0

        i = 0
        while current_code >= to_code and current_eat < to_eat:
            current_code -= slots[i][0]
            current_eat += slots[i][1]
            i += 1
           
        if current_code < to_code:
            factor = (current_eat - to_eat) / slots[i - 1][1]
            if factor > 0 and current_code + factor * slots[i - 1][0] >= to_code:
                out.append("Y")
            else:
                out.append("N")
        else:
            out.append("Y")

    print("Case #{}: {}".format(test, "".join(out)))