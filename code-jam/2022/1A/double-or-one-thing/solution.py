nof_tests = int(input())
for test in range(1, nof_tests + 1):
    string = input()
      
    pieces = []
    i = 0
    while(i < len(string)):
        # Find sequence of the same char
        c = string[i]
        seq = 0
        while i + seq < len(string) and c == string[i + seq]:
            seq += 1

        # Double when next char is greater
        if i + seq < len(string):
            next_c = string[i + seq]
            if c < next_c:
                piece = c * (2*seq)
            else:
                piece = c * (seq)
        else:
            piece = c * (seq)
        pieces.append(piece)
        
        i += seq

    print("Case #{}: {}".format(test, "".join(pieces)))