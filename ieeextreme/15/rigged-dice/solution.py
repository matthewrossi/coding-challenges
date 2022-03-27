games = int(input())

for game in range(games):
    rounds = int(input())
    first_percs = {x:0 for x in range(1,7)}
    second_percs = {x:0 for x in range(1,7)}
    exchanged=False
    total_a = 0
    total_b = 0
    for r in range(rounds):
        a, b = [int(x) for x in input().split(" ")]
        if not exchanged:
            first_add =  a
            second_add = b
        else:
            first_add = b
            second_add = a
        first_percs[first_add] += 1
        second_percs[second_add] += 1
        total_a += a
        total_b += b
        if total_a != total_b:
            exchanged= not exchanged

    first_percs = {k:v/rounds for k,v in first_percs.items()}
    second_percs = {k:v/rounds for k,v in second_percs.items()}
    
    if first_percs[6]> second_percs[6]:
        print(1)
    else:
        print(2)
