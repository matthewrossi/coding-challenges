t = int(input())
for test in range(1, t + 1):
    cj_str, jc_str, string = input().split()
    cj = int(cj_str)
    jc = int(jc_str)

    cost = 0
    prev = None
    for letter in string:
        if letter == "?":
            continue

        if prev == 'C' and letter == 'J':
            cost += cj
        elif prev == 'J' and letter == 'C':
            cost += jc
        prev = letter      
    
    print("Case #{}: {}".format(test, cost))
