nof_tests = int(input())
for test in range(1, nof_tests + 1):
    nof_consulates, nof_guests, nof_minutes = map(int, input().split())
    movement = nof_minutes % nof_consulates
    
    right_guests, left_guests = {}, {}
    right, left = [], []
    for guest in range(nof_guests):
        at, dir = input().split()
        if dir == 'C':
            pos = (int(at) + movement - 1) % nof_consulates
            if pos not in right_guests:
                right_guests[pos] = [guest]
                right.append(pos)
            else:
                right_guests[pos].append(guest)
        else:
            pos = (int(at) - movement - 1) % nof_consulates
            if pos not in left_guests:
                left_guests[pos] = [guest]
                left.append(pos)
            else:
                left_guests[pos].append(guest)
    right.sort()
    left.sort()

    right_idx = 0 
    left_idx = len(left) - 1

    nof_remember = [0 for _ in range(nof_guests)]
    right_group, left_group = {}, {}
    for i in range(nof_consulates):
        if i not in left_guests and i not in right_guests and nof_minutes:
            # nearest guests
            right_dist = (right[right_idx] - i) % nof_consulates if len(right) else 10**6
            left_dist = (i - left[left_idx]) % nof_consulates if len(left) else 10**6
            if left_dist >= right_dist and right_dist <= nof_minutes:
                # for guest in right_guests[right[right_idx]]:
                #     nof_remember[guest] += 1
                if right[right_idx] not in right_group:
                    right_group[right[right_idx]] = 1
                else:
                    right_group[right[right_idx]] += 1
            if left_dist <= right_dist and left_dist <= nof_minutes:
                # for guest in left_guests[left[left_idx]]:
                #     nof_remember[guest] += 1
                if left[left_idx] not in left_group:
                    left_group[left[left_idx]] = 1
                else:
                    left_group[left[left_idx]] += 1
        else:
            # guests at i-th consulate
            if i in right_guests:
                # for guest in right_guests[i]:
                #     nof_remember[guest] += 1
                if right[right_idx] not in right_group:
                    right_group[right[right_idx]] = 1
                else:
                    right_group[right[right_idx]] += 1
                right_idx = (right_idx + 1) % len(right)

            if i in left_guests:
                # for guest in left_guests[i]:
                #     nof_remember[guest] += 1
                if left[left_idx] not in left_group:
                    left_group[left[left_idx]] = 1
                else:
                    left_group[left[left_idx]] += 1
                left_idx = (left_idx + 1) % len(left)
    
    for pos in right:
        if pos in right_group:
            for guest in right_guests[pos]:
                nof_remember[guest] += right_group[pos]

    for pos in left:
        if pos in left_group:
            for guest in left_guests[pos]:
                nof_remember[guest] += left_group[pos]

    print("Case #{}: {}".format(test, " ".join(map(str, nof_remember))))
    