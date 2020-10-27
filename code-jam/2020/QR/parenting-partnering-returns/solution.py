from operator import itemgetter

nof_tests = int(input())
for test in range(1, nof_tests + 1):
    nof_activities = int(input())
    activities = [tuple(map(int, input().split())) for _ in range(nof_activities)]
    activities = list(enumerate(activities))
    activities.sort(key=itemgetter(1))   # on the starting time

    cameron = jamie = 0
    result = [""] * nof_activities
    for idx, activity in activities:
        start, end = activity
        if cameron <= start:
            result[idx] = "C"
            cameron = end
        elif jamie <= start:
            result[idx] = "J"
            jamie = end
        else:
            result = ["IMPOSSIBLE"]
            break

    print("Case #{}: {}".format(test, ''.join(result)))