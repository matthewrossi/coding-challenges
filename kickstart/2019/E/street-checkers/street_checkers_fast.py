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

def nof_dividers(nums, left, right): 
    all = [1 for i in range(right - left + 1)]
    odd = [1 for i in range(right - left + 1)]
    i = 0
    while (primes[i] * primes[i] <= right):
        number = left // primes[i] * primes[i]
        if left % primes[i]:
            number += primes[i]
                  
        for mul in range(number, right + 1, primes[i]): 
            add = 1
            while not nums[mul-left] % primes[i]:
                add += 1
                nums[mul-left] /= primes[i]
            all[mul-left] *= add
            if primes[i] > 2:
                odd[mul-left] *= add
        i += 1
    
    for i in range(right - left + 1): 
        if nums[i] > 1:
            all[i] *= 2
            odd[i] *= 2
    return all,odd

primes = primes_up_to(32000)

nof_tests = int(input())
for test in range(1, nof_tests + 1):
    left, right = map(int, input().split())
    nums = list(range(left, right + 1))
    all,odd = nof_dividers(nums, left, right)
    count = 0
    for i in range(right - left + 1):
        even = all[i] - odd[i]
        if (abs(even - odd[i]) <= 2):
            count += 1

    print("Case #{}: {}".format(test, count))
