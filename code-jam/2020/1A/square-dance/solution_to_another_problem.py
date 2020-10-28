# a compass neighbor is a competitior on the same row or column
# a competitor is eliminated when its skill level is lower than its compass neighbors
# a competitior without compass neighbors is never eleiminated
# competition ends when no competitor is eliminated
# interest level of a round is the sum of the skill level of competitiors
# interest level of the competition is the sum of interests levels of each round

nof_tests = int(input())
for test in range(1, nof_tests + 1):
    r, c = map(int, input().split())
    floor = [list(map(int, input().split())) for _ in range(r)]

    tot = curr = sum(map(sum, floor))
    ord_by_row = [sorted(row) for row in floor]
    row_idx = [0] * r
    ord_by_col = [sorted(col) for col in zip(*floor)]
    col_idx = [0] * c
    dancing = [[True] * c for _ in range(r)]

    change = True
    while change:
        change = False
        for i in range(r):
            row = ord_by_row[i]
            # TODO: cycle trough dancing to find two dancing competitors to compare
            if row_idx[i] + 1 < c and row[row_idx[i]] != row[row_idx[i] + 1]:
                curr -= row[row_idx[i]]
                row_idx[i] += 1
                change = True
        for i in range(r):
            col = ord_by_col[i]
            # TODO: cycle trough dancing to find two dancing competitors to compare
            if col_idx[i] + 1 < c and col[col_idx[i]] != col[col_idx[i] + 1]:
                curr -= col[col_idx[i]]
                col_idx[i] += 1
                change = True
        tot += curr
    
    print("Case #{}: {}".format(test, tot))
