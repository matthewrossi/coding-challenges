from math import sqrt
from math import floor

nof_cases = int(input())
for case in range(1, nof_cases+1):
    nof_cards = int(input())
    line = input().split(" ")
    nof_indexes = int(line[0])
    indexes = [int(s) for s in line[1:]]

    current_pos = 0
    outer_len = nof_cards
    inner_len = []
    inner_empty = []
    interval_dim = floor(sqrt(nof_cards))
    for i in range(interval_dim):
        inner_len += [interval_dim]
        inner_empty.append([j for j in range(i * interval_dim, (i+1) * interval_dim)])
    if nof_cards - interval_dim**2 > 0:
        inner_len += [nof_cards - interval_dim**2]
        inner_empty.append([j for j in range(interval_dim**2, nof_cards)])

    # if case == 69:
    #     print(inner_len)
    #     print(inner_empty)

    perfect_deck = [0 for i in range(nof_cards)]
    for card in range(nof_cards):
        # find the first empty slot after currrent position + card value
        current_pos = (current_pos + card) % outer_len
        sum = 0
        inter = inner_pos = -1

        for interval in range(len(inner_len)):
            sum += inner_len[interval]
            if current_pos < sum:
                inter = interval
                inner_pos = current_pos - (sum - inner_len[interval])
                break

        # if case == 69:
        #     print(inter, inner_pos)

        if inter >= 0 and inner_pos >= 0:
            perfect_deck[inner_empty[inter][inner_pos]] = card + 1
            del inner_empty[inter][inner_pos]
            inner_len[inter] -= 1
            outer_len -= 1
        else:
            print("Wrong")
            break

    # if case == 69:
    #     print(indexes)

    print("Case #{}:".format(case), end='')
    for index in indexes:
        print(" {}".format(perfect_deck[index - 1]), end='')
    print()
