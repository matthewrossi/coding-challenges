def backtrack_diag(trace, size, diag):
    if not size:
        #print("candidate_diag = ", diag)
        #print("trace = ", trace, "size = ", size)
        if trace:
            return []
        
        reps = [0] * (len(diag) + 1)
        for num in diag:
            reps[num] += 1

        for rep in reps:
            if rep == len(diag) - 1:
                return []   # diag not valid, try another one

        return diag         # diag valid

    max = int(trace / size)
    if max > size + len(diag):
        return []           # number not valid

    for num in range(max, 0, -1):
        ret = backtrack_diag(trace - num, size - 1, diag + [num])
        if ret:
            return ret


def backtrack_matrix(matrix, row_idx, col_idx):
    size = len(matrix)
    if col_idx == row_idx:
        row_idx += 1
        col_idx = (row_idx + 1) % size

    if row_idx == size:
            return True

    av = [False] + [True] * size
    av[matrix[row_idx][row_idx]] = False
    av[matrix[col_idx][col_idx]] = False
    for col in range(size):
        av[matrix[row_idx][col]] = False
    for row_above in range(row_idx):
        av[matrix[row_above][col_idx]] = False

    for num in range(1, size + 1):
        if av[num]:
            matrix[row_idx][col_idx] = num
            if backtrack_matrix(matrix, row_idx, (col_idx + 1) % size):
                return True

    matrix[row_idx][col_idx] = 0    # revert matrix to its previous state
    return False


nof_tests = int(input())
for test in range(1, nof_tests + 1):
    size, trace = map(int, input().split())
    # trace -> diagonal
    diagonal = backtrack_diag(trace, size, [])
    possible = True if diagonal else False
    if possible:
        # sort element in descending order
        #diagonal.sort()
        # diagonal -> natural latin square
        matrix = [[0] * size for _ in range(size)]
        for idx, num in enumerate(diagonal):
            matrix[idx][idx] = num
        backtrack_matrix(matrix, 0, 1)
        print("Case #{}: {}".format(test, "POSSIBLE"))
        for row in matrix:
            print(" ".join(map(str, row)))
    else:
        print("Case #{}: {}".format(test, "IMPOSSIBLE"))
