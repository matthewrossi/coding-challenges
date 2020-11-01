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

available_devs = list(devs)
available_pms = list(pms)

for y in range(height):
    for x in range(width):
        if not available_devs and not available_pms:
            break

        if tiles[y][x] == dev_tile and available_devs:
            available_devs[-1].x, available_devs[-1].y = x, y
            available_devs.pop(-1)
        elif tiles[y][x] == pm_tile and available_pms:
            available_pms[-1].x, available_pms[-1].y = x, y
            available_pms.pop(-1)

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