#!/usr/bin/env python3

PAYED, RECEIVED = 0, 1

def main():
    nof_tests = int(input())
    for _ in range(nof_tests):
        m = int(input())
        meals = []
        status = {}
        for _ in range(m):
            giver, nof_receivers, *receivers = input().split()
            meals.append((giver, receivers))

            # Update giver status
            giver_status = status.get(giver, [0, 0])
            giver_status[PAYED] += int(nof_receivers)
            status[giver] = giver_status

            # Update receiver status
            for receiver in receivers:
                receiver_status = status.get(receiver, [0, 0])
                receiver_status[RECEIVED] += 1
                status[receiver] = receiver_status

        nof_dinners = 0
        nof_days = 0
        for person_status in status.values():
            payed, received = person_status
            nof_dinners += max(0, received - payed)
            nof_days = max(nof_days, payed - received)

        print(nof_dinners, nof_days)


if __name__ == "__main__":
    main()