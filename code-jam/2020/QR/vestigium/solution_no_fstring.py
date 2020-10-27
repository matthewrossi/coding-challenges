# trace = sum on the main diagonal
# natural latin square = 1-to-N values with no reps across row and col
# output:
# trace + nof rows and not cols containing repeated values

def is_valid(array):
    nums = set()
    for item in array:
        if item in nums:
            return False
        nums.add(item)
    return True

nof_tests = int(input())
for test in range(1, nof_tests + 1):
    size = int(input())
    matrix = [list(map(int, input().split())) for _ in range(size)]

    k = r = c = 0
    # trace
    for idx, row in enumerate(matrix):
        k += row[idx]
    # row reps
    for row in matrix:
        if not is_valid(row):
            r += 1
    # col reps
    for col in zip(*matrix):
        if not is_valid(col):
            c += 1

    print("Case #{}: {} {} {}".format(test, k, r, c))