t = int(input())
for test in range(1, t + 1):
    str = input()
    kick = result = 0
    state_kick = state_start = 0
    for l in str:
        if l == 'K':
            if state_kick == 3:
                kick += 1
            state_kick = 1
        elif l == 'I' and state_kick == 1:
                state_kick += 1
        elif l == 'C' and state_kick == 2:
                state_kick += 1
        else:
            state_kick = 0
        if l == 'S':
            state_start = 1
        elif l == 'T' and state_start == 1:
                state_start += 1
        elif l == 'A' and state_start == 2:
                state_start += 1
        elif l == 'R' and state_start == 3:
                state_start += 1
        elif l == 'T' and state_start == 4:
            result += kick
            state_start = 0
        else:
            state_start = 0       


    print("Case #{}: {}".format(test, result))
