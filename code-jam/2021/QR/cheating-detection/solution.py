PLAYERS = 100
QUESTIONS = 10000

t = int(input())
p = int(input())
for test in range(1, t + 1):
    outcomes = [input() for _ in range(PLAYERS)]

    psolved = [0] * PLAYERS
    qsolved = [0] * QUESTIONS
    for i in range(PLAYERS):
        for j in range(QUESTIONS):
            if outcomes[i][j] == '1':
                psolved[i] += 1
                qsolved[j] += 1

    pord = sorted(range(PLAYERS), key=lambda x: psolved[x])
    qord = sorted(range(QUESTIONS), key=lambda x: qsolved[x], reverse=True)

    score = [None] * PLAYERS
    for i in range(PLAYERS):
        n0 = n1 = inv = 0
        for j in range(QUESTIONS):
            if outcomes[pord[i]][qord[j]] == '1':
                n1 += 1
                inv += n0
            else:
                n0 += 1
        inv /= n0
        inv /= n1
        score[i] = inv

    best = 0
    for i in range(1, PLAYERS):
        if score[i] > score[best]: best = i

    print("Case #{}: {}".format(test, pord[best] +1))
