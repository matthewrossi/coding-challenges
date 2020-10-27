nof_cases = int(input())
for case in range(1, nof_cases+1):
    nof_cards = int(input())
    line = input().split(" ")
    nof_indexes = int(line[0])
    indexes = [int(s) for s in line[1:]]

    current_pos = 0
    current_len = nof_cards
    empty = [i for i in range(nof_cards)]
    perfect_deck = [0 for i in range(nof_cards)]
    for card in range(nof_cards):
        # find the first empty slot after currrent position + card value
        current_pos = (current_pos + card) % current_len
        perfect_deck[empty[current_pos]] = card + 1
        del empty[current_pos]
        current_len -= 1

    print("Case #{}:".format(case), end='')
    for index in indexes:
        print(" {}".format(perfect_deck[index - 1]), end='')
    print()
