from datetime import datetime
from datetime import timedelta
from heapq import heappush, heappop

def SolveCase(case_index, case):
  T, (tripsa, tripsb) = case
  trips = []
  for trip in tripsa:
    trips.append([trip[0], trip[1], 0])
  for trip in tripsb:
    trips.append([trip[0], trip[1], 1])

  trips.sort()

  start = [0, 0]
  trains = [[], []]

  for trip in trips:
    d = trip[2]
    if trains[d] and trains[d][0] <= trip[0]:
      # We're using the earliest train available, and
      # we have to delete it from this station's trains.
      heappop(trains[d])
    else:
      # No train was available for the current trip,
      # so we're adding one.
      start[d] += 1
    # We add an available train in the arriving station at the
    # time of arrival plus the turnaround time.
    heappush(trains[1 - d], trip[1] + timedelta(minutes=T))

  print ("Case #%d: %d %d" % (case_index, start[0], start[1]))


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

    btoa = []
    for j in range(nb):  # from B to A
        departure, arrival = [str(s) for s in input().split(' ')]
        departure_t = datetime.strptime(departure, "%H:%M")
        arrival_t = datetime.strptime(arrival, "%H:%M")
        btoa.append([departure_t, arrival_t])

    case = t, (atob, btoa)

    SolveCase(i,case)
