import sys

nof_tests = int(raw_input())
for i in xrange(1, nof_tests + 1):
    nof_workers, nof_broken, max_calls = map(int, raw_input().split())
    i = 0
    while (nof_broken >> i):
        i += 1
    min_calls = i + 1

    if min_calls > max_calls:
        break

    mod = (2**min_calls)

    requests = [[0 for request in xrange(nof_workers)] for call in xrange(min_calls)]
    for i in xrange(nof_workers):
        number = i % mod
        for call in xrange(min_calls):
            request[call][i] = (number >> call) & 1
    for call in xrange(5):
        print "".join(map(str, requests[call]))
    sys.stdout.flush()

    responses = [map(int, raw_input()) for call in range(max_calls)]
    expected = id = 0
    broken = []
    for i in xrange(nof_workers):
        if id < len(responses[0]):
            number = 0
            for call in xrange(min_calls):
                number |= responses[call][i] << call
            if number != expected:
                broken.append(i)
            else:
                id += 1
            expected = (expected + 1) % mod
        else:
            broken.append(i)

    print " ".join(map(str, broken))
    sys.stdout.flush

    verdict = int(raw_input())
    if verdict != 1:
        break