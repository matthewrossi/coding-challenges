import sys

from collections import defaultdict
from collections import namedtuple


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def prefix(string):
    return string if len(sys.argv) == 1 else f"{sys.argv[1]}: {string}"


def peprint(string):
    eprint(prefix(string))


Contributor = namedtuple('Contributor', 'name nof_skills skills')
Project = namedtuple('Project', 'name duration score soft_deadline nof_roles roles_in_order roles')
Undergoing = namedtuple('Undergoing', 'project start contribs')


def next_finishing(undergoings):
    now = float("+inf")
    now_done = set()
    for p, undergoing in undergoings.items():
        project = undergoing.project
        start = undergoing.start
        end = start + project.duration
        if end < now:
            now = end
            now_done = {p}
        elif end == now:
            now_done.add(p)
    return now, now_done


# NOTE: Mentorship doesn't look like its improving anything
def get_project_contribs(project, available):
    current_available = set(available)
    current_contribs = []
    mentoriship = defaultdict(lambda: float("-inf"))
    for role, level in project.roles_in_order:
        c = None
        exists_mentor = (role in mentoriship and mentoriship[role] >= level)
        for l in range(level - exists_mentor, 11):
            if l in skill_to_contribs[role]:
                available_at_l = skill_to_contribs[role][l] & current_available
                if available_at_l:
                    c = next(iter(available_at_l))
                    current_available.remove(c)
                    current_contribs.append(c)
                    # Add new contrib as potential mentor
                    for other_skill, other_level in contribs[c].skills.items():
                        if role != other_skill:
                            mentoriship[other_skill] = max(mentoriship[other_skill], other_level)
                    break
        if c is None: return None
    return current_contribs


# NOTE: This reduces the score way more than improving it
def improve_project_contribs_skill(undergoing):
    project = undergoing.project
    for role_level, c in zip(project.roles_in_order, undergoing.contribs):
        role, level = role_level
        contrib = contribs[c]
        contrib_level = 0 if role not in contrib.skills else contrib.skills[role]
        if level - 1 <= contrib_level <= level:
            # Increase contibutor level
            if not contrib_level:
                contrib.skills[role] = 1
            else:
                contrib.skills[role] += 1
            # Update precomputed structure
            # TODO: remove level if it there are no more contribs
            skill_to_contribs[role][contrib_level].remove(c)
            current_contribs = skill_to_contribs[role].get(contrib_level + 1, set())
            current_contribs.add(c)
            skill_to_contribs[role][contrib_level + 1] = current_contribs


# Play around with it to get slight improvement in the score
def heuristic(project):
    return True


def pick_candidate_projects(projects, projects_sorted_ids, available_projects,
                            available, time):
    candidates = {}
    available = set(available)
    for p in projects_sorted_ids:
        if p in available_projects:
            project = projects[p]
            new_contribs = get_project_contribs(project, available)
            if not new_contribs:
                continue

            available.difference_update(new_contribs)
            candidates[p] = Undergoing(project, time, new_contribs)
    return candidates


def score_differential(candidates, time):
    diff = 0
    for undergoing in candidates.values():
        project = undergoing.project
        delay = max(time + project.duration - project.soft_deadline, 0)
        diff += max(project.score - delay, 0)
    return diff


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

# Preprocess set of skills
set_of_skills = {skill
                 for contrib in contribs
                 for skill in contrib.skills}

# Preprocess skill -> level -> contributors
skill_to_contribs = defaultdict(dict)
for c, contrib in enumerate(contribs):
    for skill in set_of_skills:
        level = 0 if skill not in contrib.skills else contrib.skills[skill]
        current_contribs = skill_to_contribs[skill].get(level, set())
        current_contribs.add(c)
        skill_to_contribs[skill][level] = current_contribs

# Sort project accorting to a given heuristic
projects_sorted_ids = [p for p in range(nof_projects)]
projects_sorted_ids.sort(key=lambda id: heuristic(projects[id]))

available = {c for c in range(nof_contribs)}
available_projects = {p for p in range(nof_projects)}
undergoings = dict()
done = []
time = score = 0
while True:
    # Advance time to the end of the first finishing project
    now, now_done = next_finishing(undergoings)
    if now_done:
        time = now

    # Deal with the completion of projects
    for p in now_done:
        undergoing = undergoings[p]

        # Remove project from the undergoing ones
        del undergoings[p]
        # Add project to the list of completed projects
        done.append(undergoing)

        # Make the contributors of the project available again
        available.update(undergoing.contribs)

        # Increase score
        delay = max(time - undergoing.project.soft_deadline, 0)
        score += max(undergoing.project.score - delay, 0)

    # Remove projects not worth scheduling
    available_projects = {p
                          for p in available_projects
                          if time + projects[p].duration < projects[p].soft_deadline + projects[p].score}

    now_candidates = pick_candidate_projects(projects, projects_sorted_ids,
                                             available_projects, available, time)

    # Score picking candidate projects now
    now_diff = score_differential(now_candidates, time)

    # Waiting contribs
    contribs_waiting = 0
    for undergoing in now_candidates.values():
        contribs_waiting += len(undergoing.contribs)

    # TODO: The way it is we consider the contribs in next_done without their
    # improvement, solve this by improving them at the beginning of the projects

    # Look ahead to the next step
    _next, next_done = next_finishing(undergoings)

    next_available_projects = available_projects | next_done
    next_available = available | {c for p in next_done for c in undergoings[p].contribs}
    next_candidates = pick_candidate_projects(projects, projects_sorted_ids,
                                              next_available_projects,
                                              next_available, _next)

    # Score picking candidate projects next
    wait_diff = score_differential(next_candidates, _next)

    # Schedule current candidate projects if convinient
    # NOTE: Measures cost opportunity by days spent waiting
    if now_diff + (_next - time) * contribs_waiting > wait_diff:
        for p, undergoing in now_candidates.items():
            available.difference_update(undergoing.contribs)
            available_projects.remove(p)
            #improve_project_contribs_skill(undergoing)
            undergoings[p] = undergoing
    
    if not undergoings:
        break

peprint(f"{score=}")

# Produce submission
print(len(done))
for undergoing in done:
    project = undergoing.project
    print(project.name)
    current_contribs = [contribs[c].name for c in undergoing.contribs]
    print(" ".join(current_contribs))
