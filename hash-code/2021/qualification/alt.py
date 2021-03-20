import math
import sys
from collections import namedtuple

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def prefix(string):
    return string if len(sys.argv) == 1 else f"{sys.argv[1]}: {string}"

def peprint(string):
    eprint(prefix(string))

Street = namedtuple("Street", ["start", "end", "name", "time"])
Car = namedtuple("Car", ["n", "streets"])
Intersection = namedtuple("Intersection", ["incoming"])
Schedule = namedtuple("Schedule", ["id_inter", "n", "lights"])
Light = namedtuple("Light", ["name", "duration"])


all_intersections = {}

# PARSE INPUT
duration, nof_inters, nof_streets, nof_cars, nof_bonus = map(int, input().split())

street_dict = {}
for i in range(nof_streets):
    start, end, name, time = input().split()
    start = int(start)
    end = int(end)
    time = int(time)
    street_dict[name] = Street(start, end, name, time)

cars = []
intersections = {}
for i in range(nof_cars):
    n, *streets = input().split()
    n = int(n)
    cars.append(Car(n, streets))
    for street in streets:
        street = street_dict[street]
        if street.end in intersections:
            if street in intersections[street.end].incoming:
                intersections[street.end].incoming[street] += 1
            else:
                intersections[street.end].incoming[street] = 1
        else:
            intersections[street.end] = Intersection({street: 1})

schedules = []

for index, intersection in intersections.items():
    busy = 0
    street_perc = {}
    for street, val in intersection.incoming.items():
        busy += val
        street_perc[street] = val
    for street in street_perc:
        street_perc[street] = street_perc[street]/ busy
    lights = []
    for street, perc in street_perc.items():
        light = Light(street.name, math.ceil(len(intersection.incoming) * perc))
        lights.append(light)
    schedule = Schedule(index, len(lights), lights)
    schedules.append(schedule)


# PRODUCE SUBMISSION
print(len(schedules))
for schedule in schedules:
    print(schedule.id_inter)
    print(schedule.n)
    for light in schedule.lights:
        print(light.name, light.duration)