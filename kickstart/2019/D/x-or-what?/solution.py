# even xor even => even
# odd xor odd => even
# even xor odd / odd xor even => odd

def is_odd(num):
    count = 0
    for j in xrange(10): # up to 1024
        if (num >> j) & 1:
            count += 1
    return count & 1

def first(array, value):
    for i in xrange(len(array)):
        if array[i] == value:
            return i
    return -1

nof_tests = int(raw_input())
for test in xrange(nof_tests):
    nof_ints, nof_mods = map(int, raw_input().split())
    array = map(int, raw_input().split())
    changes = [map(int, raw_input().split()) for __ in xrange(nof_mods)]

    odd = [False for __ in xrange(nof_ints)]
    for i in xrange(nof_ints):
        odd[i] = is_odd(array[i])
    
    intervals = []
    for i in xrange(nof_mods):
        odd[changes[i][0]] = is_odd(changes[i][1])

        if sum(odd) & 1:
            intervals.append(nof_ints - min(first(odd, True), first(odd[::-1], True)) - 1)
        else:
            intervals.append(nof_ints)

    print "Case #{}: {}".format(test + 1, " ".join(map(str, intervals)))
