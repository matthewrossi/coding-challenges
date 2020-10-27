# a compass neighbor is a competitior on the same row or column and no other competitiors
# between them
# a competitor is eliminated when its skill level is lower than the average of its compass
# neighbors
# a competitior without compass neighbors is never eleiminated
# competition ends when no competitor is eliminated
# interest level of a round is the sum of the skill level of competitiors
# interest level of the competition is the sum of interests levels of each round

class Dancer:
    def __init__(self, skill, cns):
        self.skill = skill  # skill level
        self.cns = cns      # compass neighbors - left, top, right, down

nof_tests = int(input())
for test in range(1, nof_tests + 1):
    r, c = map(int, input().split())
    skills = [list(map(int, input().split())) for _ in range(r)]

    # create adjacency list
    dancers = [None] * (r * c)
    for i in range(r):
        for j in range(c):
            curr = i * c + j
            dancers[curr] = Dancer(
                skills[i][j],
                [
                    curr - 1 if j else -1,
                    curr - c if i else -1,
                    curr + 1 if j + 1 < c else -1,
                    curr + c if i + 1 < r else -1
                ]
            )

    # compute 1st round interest
    tot = curr = sum(map(sum, skills))

    changed = set(range(r * c))
    while changed:
        # reduce round interest
        to_remove = set()
        for idx in changed:
            dancer = dancers[idx]
            cum = n = 0
            for cn in dancer.cns:
                if cn != -1:
                    cum += dancers[cn].skill
                    n += 1
            if n and dancer.skill < cum / n:
                to_remove.add(idx)
                curr -= dancer.skill

        # previous round was the last one
        if not to_remove:
            break

        # increment contest interest by the round interest
        tot += curr        
        # remove eliminated dancers
        changed = set()
        for idx in to_remove:
            dancer = dancers[idx]
            left, top, right, down = dancer.cns
            if left != -1:
                dancers[left].cns[2] = right
                changed.add(left)
            if top != -1:
                dancers[top].cns[3] = down
                changed.add(top)
            if right != -1:
                dancers[right].cns[0] = left
                changed.add(right)
            if down != -1:
                dancers[down].cns[1] = top
                changed.add(down)
        # do not consider as changed removed dancers
        changed -= to_remove

    print("Case #{}: {}".format(test, tot))
