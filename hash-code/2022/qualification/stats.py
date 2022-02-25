#!/usr/bin/env python

import matplotlib.pyplot as plt
import sys

from collections import defaultdict
from collections import namedtuple



def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def prefix(string):
    return string if len(sys.argv) == 1 else f"{sys.argv[1]}: {string}"


def peprint(string):
    eprint(prefix(string))


def distrib(dictionary, path):
    # Sort bars by values when keys are strings
    keys = list(dictionary.keys())
    values = list(dictionary.values())
    if keys and isinstance(keys[0], str):
        ids = [i for i in range(len(keys))]
        ids.sort(key=lambda i: values[i], reverse=True)
        keys = [keys[i] for i in ids]
        values = [values[i] for i in ids]

    fig, ax = plt.subplots()
    ax.bar(keys, values)
    fig.savefig(path)
    #plt.show()


Contributor = namedtuple('Contributor', 'name nof_skills skills')
Project = namedtuple('Project', 'name duration score soft_deadline nof_roles roles_in_order roles')


# Read dataset identifier as argument
dataset = "" if len(sys.argv) == 1 else sys.argv[1]

# Parse input
nof_contribs, nof_projects = map(int, input().split())

contribs = [None] * nof_contribs
for c in range(nof_contribs):
    name, nof_skills = input().split()
    nof_skills = int(nof_skills)
    skills = {}
    for _ in range(nof_skills):
        skill, level = input().split()
        level = int(level)
        skills[skill] = level
    contribs[c] = Contributor(name, nof_skills, skills)
projects = [None] * nof_projects
for p in range(nof_projects):
    name, *stuff = input().split()
    duration, score, soft_deadline, nof_roles = map(int, stuff)
    roles = defaultdict(list)
    roles_in_order = []
    for _ in range(nof_roles):
        skill, level = input().split()
        level = int(level)
        roles[skill].append(level)
        roles_in_order.append((skill, level))
    projects[p] = Project(name, duration, score, soft_deadline, nof_roles, roles_in_order, roles)

# Contributors
by_nof_skills = defaultdict(int)
by_skills = defaultdict(int)
for contrib in contribs:
    by_nof_skills[contrib.nof_skills] += 1
    for skill, _ in contrib.skills.items():
        by_skills[skill] += 1

peprint(f"[*] Number of contributors: {nof_contribs}")
peprint(f"\n[*] Number of unique skills: {nof_skills}")
peprint("\n[*] Contributors by #skills")
peprint(by_nof_skills)
distrib(by_nof_skills, f"analysis/{dataset}_by_nof_skills.pdf")
peprint("\n[*] Contributors by skills")
peprint(by_skills)
distrib(by_skills, f"analysis/{dataset}_by_skills.pdf")
# TODO: For each skill show the level distribution

# Projects
by_score = defaultdict(int)
by_deadline = defaultdict(int)
by_nof_roles = defaultdict(int)
by_roles = defaultdict(int)
for project in projects:
    by_score[project.score] += 1
    by_deadline[project.soft_deadline] += 1
    by_nof_roles[project.nof_roles] += 1
    for role, _ in project.roles_in_order:
        by_roles[role] += 1

peprint(f"\n\n[*] Number of projects: {nof_projects}")
peprint("\n[*] Projects by score")
peprint(by_score)
distrib(by_score, f"analysis/{dataset}_by_score.pdf")
peprint("\n[*] Projects by soft deadline")
peprint(by_deadline)
distrib(by_deadline, f"analysis/{dataset}_by_deadline.pdf")
peprint("\n[*] Projects by #roles")
peprint(by_nof_roles)
distrib(by_nof_roles, f"analysis/{dataset}_by_nof_roles.pdf")
peprint("\n[*] Projects by roles")
peprint(by_roles)
distrib(by_roles, f"analysis/{dataset}_by_roles.pdf")
# TODO: For each skill show the level distribution
