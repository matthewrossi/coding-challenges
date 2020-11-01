from collections import defaultdict
from operator import itemgetter

class Replyer(object):
    def __init__(self, company, bonus, nof_skills, skills):
        self.company = company
        self.bonus = bonus
        self.nof_skills = nof_skills
        self.skills = skills
        self.x = -1
        self.y = -1

def fill(rep, tile_type):
    x, y = 0, 0
    idx = 0
    for y in range(height):
        for x in range(width):
            if idx == len(rep):
                return

            if tiles[y][x] != busy_tile and tiles[y][x] == tile_type:
                rep[idx].x, rep[idx].y = x, y
                idx += 1

width, height = map(int, input().split())
tiles = [input() for row in range(height)]

busy_tile = '#'
dev_tile = '_'
pm_tile = 'M'

nof_devs = int(input())
devs = []
company_replyers = defaultdict(list)
skill_replyers = defaultdict(list)
for idx in range(nof_devs):
    company, bonus, nof_skills, *skills = input().split()
    bonus = int(bonus)
    nof_skills = int(nof_skills)

    devs.append(Replyer(company, bonus, nof_skills, skills))
    company_replyers[company].append(idx)
    for idx in range(nof_skills):
        skill_replyers[skills[idx]].append(idx)

nof_pms = int(input())
pms = []
for _ in range(nof_pms):
    company, bonus = input().split()
    bonus = int(bonus)
    pms.append(Replyer(company, bonus, None, None))

fill(devs, dev_tile)
fill(pms, pm_tile)

for idx in range(nof_devs):
    if devs[idx].x != -1:
        print(devs[idx].x, devs[idx].y)
    else:
        print("X")

for idx in range(nof_pms):
    if pms[idx].x != -1:
        print(pms[idx].x, pms[idx].y)
    else:
        print("X")