ROW = 0
CELLS = 1

BLOCKS = ["+-", "|."]


def line(kind, is_first, size):
    block = BLOCKS[kind]

    pieces = [".."] if is_first else [block]
    for _ in range(size - 1):
        pieces.append(block)
    pieces.append(block[0])

    return "".join(pieces)


nof_test = int(input())
for test in range(1, nof_test + 1):
    r, c = map(int, input().split())

    lines = [line(ROW, True, c), line(CELLS, True, c)]
    for _ in range(r - 1):
        lines.extend([line(ROW, False, c), line(CELLS, False, c)])
    lines.append(line(ROW, False, c))

    print("Case #{}: \n{}".format(test, "\n".join(lines)))
