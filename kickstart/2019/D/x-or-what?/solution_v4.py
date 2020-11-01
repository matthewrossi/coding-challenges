# even xor even => even
# odd xor odd => even
# even xor odd / odd xor even => odd

def is_odd(num):
    count = 0
    for j in xrange(10): # up to 1024
        if (num >> j) & 1:
            count += 1
    return count & 1

nof_tests = int(raw_input())
for test in xrange(nof_tests):
    nof_ints, nof_mods = map(int, raw_input().split())
    array = map(int, raw_input().split())
    changes = [map(int, raw_input().split()) for __ in xrange(nof_mods)]

    odd = [False for __ in xrange(nof_ints)]

    count = 0
    first = last = -1
    for i in xrange(nof_ints):
        odd[i] = is_odd(array[i])
        if odd[i]:
            if first == -1: first = i
            last = i
            count += 1
    
    intervals = []
    for i in xrange(nof_mods):
        odd_change = is_odd(changes[i][1])
        if odd[changes[i][0]] != odd_change:
            odd[changes[i][0]] = odd_change
            if odd_change:
                count += 1
                if changes[i][0] < first or first == -1:
                    first = changes[i][0]
                if changes[i][0] > last:
                    last = changes[i][0]
            else:
                count -= 1
                if not count:
                    first = last = -1
                elif count == 1:
                    if changes[i][0] == first:
                        first = last
                    else:
                        last = first
                else:
                    if changes[i][0] == first:
                        found = False
                        j = changes[i][0] + 1
                        while(not found and j < nof_ints):
                            if odd[j]:
                                first = j
                                found = True
                            j += 1                    
                    elif changes[i][0] == last:
                        found = False
                        j = changes[i][0] - 1
                        while(not found and j > 0):
                            if odd[j]:
                                last = j
                                found = True
                            j -= 1

        if count & 1:
            intervals.append(max(last, nof_ints - first - 1))
        else:
            intervals.append(nof_ints)

    print "Case #{}: {}".format(test + 1, " ".join(map(str, intervals)))
