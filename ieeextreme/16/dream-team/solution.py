#!/usr/bin/env python3

"""Wrong Answer"""

import itertools

NOF_ROLES = 5
NAME, COST = 0, 1

def main():
    budget = int(input())

    roles = []
    for _ in range(NOF_ROLES):
        nof_players = int(input())
        players = []
        for _ in range(nof_players):
            name, cost = input().split()
            cost = int(cost)
            players.append((name, cost))
        players.sort(key=lambda x: x[1])
        roles.append(players)

    best_residual = budget
    best_team = []
    for roles_order in itertools.permutations(range(NOF_ROLES)):
        # print("New role order:", roles_order)

        curr_residual = budget
        curr_team = [-1] * NOF_ROLES
        incomplete_team = False
        for role in roles_order:
            players = roles[role]

            # Check possibility to pick a player
            _, cost = players[0]
            if cost > curr_residual:
                incomplete_team = True
                break

            # Find best affordable player
            for player_id, player in enumerate(players):
                name, cost = player
                if cost > curr_residual:
                    curr_team[role] = player_id - 1
                    break

            # print(f"Budget: {curr_residual}, Role: {role}, Player_id: {curr_team[role]}, Player: {players[curr_team[role]]}")

            # Update budget according to the best affordable player
            curr_residual -= players[curr_team[role]][COST]
            assert curr_residual >= 0

        # Keep track of the best team composition
        if not incomplete_team and best_residual > curr_residual:
            best_residual = curr_residual
            best_team = curr_team
            # print(f"New best residural: {best_residual}, New best team: {best_team}")
       
    names = [roles[role][player_id][NAME] for role, player_id in enumerate(best_team)]
    print("\n".join(names))


if __name__ == "__main__":
    main()