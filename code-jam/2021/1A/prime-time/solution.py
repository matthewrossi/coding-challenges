#!/usr/bin/env python3

t = int(input())
for test in range(1, t + 1):
    m = int(input())
    cards = [tuple(map(int, input().split())) for _ in range(m)]

    # compute the sum of all the numbers
    total = 0
    for i in range(m):
        value, rep = cards[i]
        total += value * rep
    
    # possibe sums are between X - 29940 and X
    for exp in range(2, 29941):
        num = total - exp
        if num < 2:
            break

        # factorize number with the given primes when possible
        factors = [None] * m
        for i in range(m):
            value, rep = cards[i]

            count = 0
            while count < rep and num % value == 0:
                num /= value
                count += 1
            factors[i] = count

        if num == 1:
            # check the sum of the factors against expectation
            rsum = 0
            for i, rep in enumerate(factors):
                if rep is not None:
                    value, _ = cards[i]
                    rsum += value * rep

            if exp == rsum:
                break

    score = total - rsum if exp == rsum else 0
    print("Case #{}: {}".format(test, score))
