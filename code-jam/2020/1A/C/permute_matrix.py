from itertools import permutations

r = c = 3
elements = list(1, range(10))

tests = len(permutations(elements))
for perm in permutations(elements):
    matrix = []
    for i in range(r):
        matrix.append(perm[i*c:(i + 1)*c])
    
    # ...
