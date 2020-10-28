def mirror(path):
    my_path = ""
    for move in path:
        if (move == 'E'):
            my_path += 'S'
        else:
            my_path += 'E'
    return my_path

t = int(raw_input())  # read number of tests
for i in xrange(1, t + 1):
    size = int(raw_input())  # read the maze size
    path = raw_input()
    print "Case #{}: {}".format(i, mirror(path))