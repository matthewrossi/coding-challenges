from datetime import datetime
from datetime import timedelta


def argmin(array, starting_at):
    min = datetime.strptime("23:59", "%H:%M")
    argmin = -1
    for i in range(starting_at, len(array)):
        if min > array[i][1]:
            min = array[i][1]
            argmin = i
    return argmin, min


def binary_search(array, x):
    if len(array) > 0:
        return binary_search_inner(array, 0, len(array) - 1, x)
    return -1


def binary_search_inner(array, start, end, x):
    while start < end:
        center = int((start + end) / 2)
        if array[center][0] >= x:
            end = center
        else:
            start = center + 1
    if end < len(array) and array[end][0] >= x:
        return end
    else:
        return -1


n = int(input())
for i in range(1, n + 1):
    t = int(input())
    na, nb = [int(s) for s in input().split(' ')]

    atob = []
    for j in range(na):  # from A to B
        departure, arrival = [str(s) for s in input().split(' ')]
        departure_t = datetime.strptime(departure, "%H:%M")
        arrival_t = datetime.strptime(arrival, "%H:%M")
        atob.append([departure_t, arrival_t])
    atob.sort()

    btoa = []
    for j in range(nb):  # from B to A
        departure, arrival = [str(s) for s in input().split(' ')]
        departure_t = datetime.strptime(departure, "%H:%M")
        arrival_t = datetime.strptime(arrival, "%H:%M")
        btoa.append([departure_t, arrival_t])
    btoa.sort()

    a_trains = 0
    b_trains = 0
    while len(atob) > 0 and len(btoa) > 0:
        to_b_index, to_b_value = argmin(atob, 0)
        to_a_index, to_a_value = argmin(btoa, 0)

        if to_b_value < to_a_value:  # start with A to B
            a_trains += 1
            while (True):
                del atob[to_b_index]
                starting_at = binary_search(btoa, to_b_value+timedelta(minutes=t))
                if starting_at >= 0:
                    to_a_index, to_a_value = argmin(btoa, starting_at)
                    del btoa[to_a_index]
                    starting_at = binary_search(atob, to_a_value+timedelta(minutes=t))
                    if starting_at >= 0:
                        to_b_index, to_b_value = argmin(atob, starting_at)
                    else:
                        break
                else:
                    break

        else:  # start with B to A
            b_trains += 1
            while (True):
                del btoa[to_a_index]
                starting_at = binary_search(atob, to_a_value+timedelta(minutes=t))
                if starting_at >= 0:
                    to_b_index, to_b_value = argmin(atob, starting_at)
                    del atob[to_b_index]
                    starting_at = binary_search(btoa, to_b_value+timedelta(minutes=t))
                    if starting_at >= 0:
                        to_a_index, to_a_value = argmin(btoa, starting_at)
                    else:
                        break
                else:
                    break

    # fill the missing trips with new trains
    a_trains += len(atob)
    b_trains += len(btoa)

    print("Case #{}: {} {}".format(i, a_trains, b_trains))
