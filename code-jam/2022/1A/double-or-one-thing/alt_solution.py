nof_tests = int(input())
for test in range(1, nof_tests + 1):
    string = input()
    
    tokens = []
    prev = None
    counter = 1
    for c in string:
        if prev is not None:
            if c != prev:
                tokens.append((prev, counter))
                counter = 1
            else:
                counter += 1
        prev = c
    tokens.append((prev, counter))

    pieces = []
    for i, token  in enumerate(tokens[:-1]):
        c, reps = token
        next_c, _ = tokens[i + 1]
        if c < next_c:
            piece = c * (2 * reps)
        else:
            piece = c * reps
        pieces.append(piece)
    c, reps = tokens[-1]
    pieces.append(c * reps)

    print("Case #{}: {}".format(test, "".join(pieces)))