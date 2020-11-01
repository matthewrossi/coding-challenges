# 4 keys
# 1st note any key
# if higher(lower) pitch use higher(lower) pitch key (what if i end the keys)
# if equal pitch use the same key
# how many times does he has to break the rule?
# number of increasing(decreasing) pitch greater than multiple of 4 (excluding =)

KEYS = 4

t = int(input())
for test in range(1, t + 1):
    n = int(input())
    notes = list(map(int, input().split()))

    inc = dec = result = 0
    for i in range(len(notes) - 1):
        if notes[i] < notes[i + 1]:
            if dec >= KEYS:
                result += dec // KEYS
            dec = 0  # waste 
            inc += 1
        elif notes[i] > notes[i + 1]:
            if inc >= KEYS:
                result += inc // KEYS
            inc = 0  # waste
            dec += 1

    if dec >= KEYS:
        result += dec // KEYS
    if inc >= KEYS:
        result += inc // KEYS
    
    print("Case #{}: {}".format(test, result))

