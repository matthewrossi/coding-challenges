def split(n):

    # force remainder > 0
    n -= 1
    remainder = 1

    n = str(n)
    length = len(n)

    for i in range(length):
        if n[i] == '4':
            n = n[:i] + '3' + n[(i + 1):]
            remainder += 10**(length - i - 1)           

    return n, remainder

t = int(input())  # read number of tests
for i in xrange(1, t + 1):
    n = int(raw_input())  # read number
    a, b = split(n)
    print ("Case #{}: {} {}".format(i, a, b))