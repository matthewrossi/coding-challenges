T = int(input())
for i in range(1, T+1):
    row = input()
    R, C = int(row.split(" ")[0]), int(row.split(" ")[1])
    initials = {}
    cake = [['' for c in range(C)] for r in range(R)]
    for r in range(R):
        row = input()
        for c in range(C):
            if row[c] != '?':
                initials[row[c]] = r,c
            cake[r][c] = row[c]

    last_row = []
    prev_empty_row = 0
    for r in range(R):
        # fill the row if at least one character is there
        last_char = ''
        prev_empty_char = 0
        for c in range(C):
            if cake[r][c] != '?':
                last_char = cake[r][c]
                if prev_empty_char > 0:
                    for j in range(1, prev_empty_char+1):
                        cake[r][c-j] = last_char
                        prev_empty_char = 0
            elif last_char != '':
                cake[r][c] = last_char
            else:
                prev_empty_char += 1

        # handle empty row
        if prev_empty_char == 0:
            last_row = cake[r]
            if prev_empty_row > 0:
                for j in range(1, prev_empty_row + 1):
                    cake[r - j] = last_row
                prev_empty_row = 0
        elif last_row != []:
            cake[r] = last_row
        else:
            prev_empty_row += 1

    print("Case #{}:".format(i))
    for r in range(R):
        for c in range(C):
    	    print(cake[r][c], end='')
        print()
