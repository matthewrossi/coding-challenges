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


def best_match(reps, x, y):
    up = who[y - 1][x] if y - 1 > 0 else None
    left = who[y][x - 1] if x - 1 > 0 else None

    if not up and not left:
        return 0

    max_idx, max_value = 0, 0
    for idx in range(len(reps)):
        current_value = 0
        if up:          
            current_value += compute_value(reps[idx], up)
        if left:
            current_value += compute_value(reps[idx], left)

        if max_value < current_value:
            max_value = current_value
            max_idx = idx

    return max_idx        


def compute_value(a, b):
    value = 0

    if a.skills and b.skills:
        common_skills = len(a.skills.intersection(b.skills))
        not_common_skills = len(a.skills.union(b.skills) - a.skills.intersection(b.skills))
        value += common_skills * not_common_skills

    if a.company == b.company:
        value += a.bonus * b.bonus

    return value    


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
    skills = set(skills)
    nof_skills = int(nof_skills)

    devs.append(Replyer(company, bonus, nof_skills, skills))
    company_replyers[company].append(idx)
    for skill in skills:
        skill_replyers[skill].append(idx)

nof_pms = int(input())
pms = []
for _ in range(nof_pms):
    company, bonus = input().split()
    bonus = int(bonus)
    pms.append(Replyer(company, bonus, None, None))

who = []
for y in range(height):
    who.append([])
    for x in range(width):
        who[y].append(None)

available_devs = list(devs)
available_pms = list(pms)

for y in range(height):
    for x in range(width):
        if not available_devs and not available_pms:
            break

        if tiles[y][x] == dev_tile and available_devs:
            devs_idx = best_match(available_devs, x, y)
            available_devs[devs_idx].x, available_devs[devs_idx].y = x, y
            dev = available_devs.pop(devs_idx)
            who[y][x] = dev
        elif tiles[y][x] == pm_tile and available_pms:
            pms_idx = best_match(available_pms, x, y)
            available_pms[pms_idx].x, available_pms[pms_idx].y = x, y
            pm = available_pms.pop(pms_idx)
            who[y][x] = pm

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
