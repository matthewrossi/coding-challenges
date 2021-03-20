import math
import random
import sys

from collections import defaultdict, namedtuple

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def prefix(string):
    return string if len(sys.argv) == 1 else f"{sys.argv[1]}: {string}"

def peprint(string):
    eprint(prefix(string))

Schedule = namedtuple("Schedule", ["id_inter", "n", "lights"])
Light = namedtuple("Light", ["name", "duration"])

class Car:
    def __init__(self, n, path):
        self.n = n
        self.path = path
        self.time_to_complete = None

class Intersection:
    def __init__(self, idx, incoming, outgoing):
        self.idx = idx
        self.incoming = incoming
        self.outgoing = outgoing

class Street:
    def __init__(self, start, end, name, time):
        self.start = start
        self.end = end
        self.name = name
        self.time = time
        self.freq = 0

# PARSE INPUT
duration, nof_inters, nof_streets, nof_cars, bonus = map(int, input().split())

streets = {}
inters = {}
for i in range(nof_streets):
    start, end, name, time = input().split()
    start = int(start)
    end = int(end)
    time = int(time)
    streets[name] = Street(start, end, name, time)
    # add outgoing street to intersection
    if start not in inters:
        inters[start] = Intersection(start, [], [name])
    else:
        inters[start].outgoing.append(name)
    # add incoming street to intersection
    if end not in inters:
        inters[end] = Intersection(start, [name], [])
    else:
        inters[end].incoming.append(name)

cars = []
for i in range(nof_cars):
    n, *path = input().split()
    n = int(n)
    cars.append(Car(n, path))

# macchine che non arrivano
for car in cars:
    car.time_to_complete = 0
    for name in car.path:
        car.time_to_complete += streets[name].time
    
    if car.time_to_complete <= duration:
        for street in car.path:
            streets[street].freq += (duration - car.time_to_complete) / duration

# SOLVE
schedules = []

tot1 = tot2 = 0
for id, inter in inters.items():
    lights = []
    to_schedule = [name for name in inter.incoming if streets[name].freq]
    if len(to_schedule) == 1:
        lights.append(Light(to_schedule[0], duration))
    else:
        tot = 0
        for name in to_schedule:
            tot += streets[name].freq
        for name in to_schedule:
            perc = streets[name].freq / tot
            rotation_time = math.floor(duration / 1000)
            if len(to_schedule) > 3:
                lights.append(Light(name, min(math.ceil(perc * rotation_time) + 1, duration)))
                tot1 += 1
            else:
                lights.append(Light(name, 1))
            tot2+= 1

    if len(to_schedule):
        schedules.append(Schedule(id, len(to_schedule), lights))

peprint(f"molto traffico: {tot1}")
peprint(f"poco traffico: {tot2}")

# COMPUTE THE SOLUTION SCORE
# anche no

# PRODUCE SUBMISSION
print(len(schedules))
for schedule in schedules:
    print(schedule.id_inter)
    print(schedule.n)
    for light in schedule.lights:
        print(light.name, light.duration)
