from math import floor

def is_prime(number, lower_primes):
    upper_pos = upper_bound_search(lower_primes, number**0.5)
    if upper_pos == -1:
        lower_primes = []
    else:
        lower_primes = lower_primes[:(upper_pos+1)]

    for divider in lower_primes:
        if number % divider == 0:
            return False
    return True


# Too slow
def primes_up_to(limit):    # standard way
    primes = []
    for number in range(2, limit + 1):  # to be inclusive
        if is_prime(number, primes):
            primes.append(number)
    return primes


# MemoryError
def sieve(limit):    # based on sieve of Eratosthenes
    is_prime = [True] * (limit+1) # let's avoid the -2 op at a cost of 2 more memory slots
    for number in range(2, floor(limit**0.5) + 1):  # +1 to be inclusive
        if is_prime[number]:
            for mul in range(number*number, limit+1, number):
                is_prime[mul] = False

    primes = []
    for number in range(2, limit + 1):  # +1 to be inclusive
        if is_prime[number]:
            primes.append(number)
    return primes


# Avoid MemoryError by doing the same job batch by batch
def segmented_sieve(size, limit):    # based on sieve of Eratosthenes
    # Handles the fist batch
    if size < limit:
        primes = sieve(size - 1)
    else:
        primes = sieve(limit)

    actual_size = size
    for i in range(1, (limit + size - 1) // size):
        min = size * i
        if i < (limit + size - 1) // size - 1:
            max = size * (i + 1) - 1
            is_prime = [True] * size
        else:
            # Handles the last batch
            max = limit
            actual_size = max - min + 1
            is_prime = [True] * actual_size

        upper_pos = upper_bound_search(primes, max ** 0.5)
        if upper_pos >= 0:
            our_primes = primes[:(upper_pos + 1)]
        else:
            our_primes = []

        # Removes multiple of previous primes
        for prime in our_primes:
            for j in range(((min + prime - 1) // prime) * prime - min, actual_size, prime):
                is_prime[j] = False

        # Removes multiple of new primes
        for j in range(floor(max**0.5) - min + 1):
            if is_prime[j]:
                number = j + min
                for k in range(number*number - min, actual_size, number):
                    is_prime[k] = False

        for j in range(actual_size):
            if is_prime[j]:
                primes.append(j + min)

    return primes


def lower_bound_search(primes, lower_bound):    # inclusive w/o considering unicity
    start = 0
    end = len(primes) - 1
    while start < end:
        center = (start + end) // 2
        if primes[center] < lower_bound:
            start = center + 1
        else:
            end = center
    if end < 0 or primes[end] < lower_bound:
        return -1
    return end


def upper_bound_search(primes, upper_bound):    # inclusive w/o considering unicity
    start = 0
    end = len(primes) - 1
    while start < end:
        center = (start + end + 1) // 2
        if primes[center] > upper_bound:
            end = center - 1
        else:
            start = center
    if end < 0 or primes[end] > upper_bound:
        return -1
    return end


def restrict_primes(primes, lower_bound, upper_bound):
    lower_pos = lower_bound_search(primes, lower_bound)
    upper_pos = upper_bound_search(primes, upper_bound)
    if lower_pos == -1 or upper_pos == -1 or lower_pos > upper_pos:
        return []
    else:
        return primes[lower_pos:(upper_pos+1)]


def share_prime(list1, list2):
    for prime1 in list1:
        for prime2 in list2:
            if len(range((A + prime1*prime2 - 1) // (prime1*prime2), B // (prime1*prime2) + 1)) > 0:
                return True
    return False


small_dataset = 1000
large_dataset = 10**12

# compute the possible primes in the dataset
primes = sieve(small_dataset // 2)
#primes = segmented_sieve(floor(large_dataset**0.5), large_dataset // 2)

nof_cases = int(input())
for case in range(1, nof_cases+1):
    A, B, P = [int(s) for s in input().split(" ")]
    # restrict the primes based on the lower and upper bound given
    our_primes = restrict_primes(primes, P, B)

    # create initial sets
    singletons = set(range(A, B + 1))
    sets = []
    for prime in our_primes:
        elements = range(((A + prime - 1) // prime) * prime, B + 1, prime)
        if len(elements) > 0:
            singletons = singletons.difference(set(elements))
            sets.append([prime])

    # build up bigger sets
    i = 0
    while i < len(sets):
        for j in range(i + 1, len(sets)):
            if share_prime(sets[i], sets[j]):
                sets.append(sets.pop(i) + sets.pop(j - 1))  # -1 due to the removal of the previous i-th element
                # start the cycle back considering a new element
                i -= 1
                break
        i += 1

    print("Case #{}: {}".format(case,len(singletons)+len(sets)))
