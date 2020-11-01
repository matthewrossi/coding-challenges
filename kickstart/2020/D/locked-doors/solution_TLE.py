# 1 to N rooms in a row
# N-1 locked doors connect the adjacent rooms
# each door has a unique difficulty level

# start room, goes to lower difficulty, if only one locked, opens it
# once a door is unlocked it remains so

# queries: K-th room she visits starting from S-th

t = int(input())
for test in range(1, t + 1):
    n, q = map(int, input().split())
    doors = list(map(int, input().split()))
    queries = [tuple(map(int, input().split())) for _ in range(q)]

    prev_res = {}
    answer = []
    for query in queries:
        if query not in prev_res:
            current, step = query
            left = current - 2
            right = current - 1
            for i in range(step - 1):
                if left < 0 or (right != n - 1 and doors[left] > doors[right]):
                    current = right + 2
                    right += 1
                else:
                    current = left + 1
                    left -= 1
            prev_res[query] = current
        answer.append(str(prev_res[query]))

    print("Case #{}: {}".format(test, " ".join(answer)))
