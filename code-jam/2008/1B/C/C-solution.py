nof_cases = int(input())
for case in range(1, nof_cases+1):
    nof_cards = int(input())
    line = input().split(" ")
    nof_indexes = int(line[0])
    indexes = [int(s) for s in line[1:]]

    deck = [-1] * (nof_cards+1) # 0 position not used

    # compute the tree dimension
    internal_nodes = 1
    while internal_nodes < nof_cards:
        internal_nodes *= 2

    # set the tree
    tree = [1] * (2 * internal_nodes)   # leaves are correctly set
    for i in range(internal_nodes - 1, 0, -1):  # set up the internal nodes
        tree[i] = tree[2*i] + tree[2*i+1]

    for card in range(1, nof_cards+1):
        places = nof_cards - card + 1   # available places to put the card
        l = card % places   # number of places we need to "jump"
        if l == 0:
            l += places

        if card == 1:
            j = 1   # position where the card will be placed
        else:
            o = internal_nodes + j  # interval that follows the last placed card
            # count the places we have left before the selected interval
            lc = 0
            while o > 1:
                if o % 2:
                    o //= 2
                    lc += tree[2*o]
                else:
                    o //= 2
            lc += l         # increment it by the number of places we need to "jump"
            lc %= places    # start the deck over if we get to the end of the deck
            if lc == 0:
                lc += places

            # find the new interval where to put the card
            j = 1
            while j < internal_nodes:
                if tree[2*j] >= lc:
                    j = 2*j
                else:
                    lc -= tree[2*j]
                    j = 2*j+1
            # convert it to a card spot by subtracting the nof internal nodes
            j -= (internal_nodes - 1)

        # update the tree reducing the number of available places to put the card
        o = internal_nodes - 1 + j
        while o >= 1:
            tree[o] -= 1
            o //= 2

        # place the card
        deck[j] = card

    print("Case #{}:".format(case), end='')
    for index in indexes:
        print(" {}".format(deck[index]), end='')
    print()
