def primes_up_to(n): 
    prime = [True for i in range(n + 1)] 
    p = 2
    while (p * p <= n): 
        if (prime[p] == True):               
            for i in range(p * 2, n + 1, p): 
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    
    primes = []
    for p in range(n + 1): 
        if prime[p]:
            primes.append(p)
    return primes

from math import sqrt

def is_multiple(number, dividers):
    max = sqrt(number)
    for div in dividers:
        if div > max:
            return False
        if not number % div:
            return True
    return False

odds = primes_up_to(10**3)[1:]  # 32000

nof_tests = int(input())
for test in range(1, nof_tests + 1):
    left, right = map(int, input().split())
    count = 0

    for number in range(left, right + 1):
        i = 1
        while not number % 2**i and i <= 4:
            i += 1
        i -= 1

        if i == 0:
            # odd dividers: 1, ?, number
            if not is_multiple(number, odds):
                count += 1
        elif i == 1:
            # same nof even and odd dividers
            count += 1
        elif i == 2:
            # odd dividers: 1, ?, number / 4
            if number == 4:
                count += 1
            else:
                if not is_multiple(number / 4, odds):
                    count += 1
        elif i == 3 and number == 8:
            # odd dividers: 1, number / 8
            count += 1
        # i > 3 unfair

    print("Case #{}: {}".format(test, count))
    