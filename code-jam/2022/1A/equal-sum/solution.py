import math

MIN_NUM = 1
MAX_NUM = 10**9
MAX_POWER_OF_2 = math.ceil(math.log(10**9, 2))


def fill_sets(numbers, a, b):
    sum_a = sum(a)
    sum_b = sum(b)

    for number in numbers:
        if sum_a <= sum_b:
            a.add(number)
            sum_a += number
        else:
            b.add(number)
            sum_b += number


nof_tests = int(input())
for test in range(1, nof_tests + 1):
    n = int(input())    # 100 > MAX_POWER_OF_2

    # Send our set of numbers
    powers = [2**i for i in range(MAX_POWER_OF_2)]

    powers_as_set = set(powers)
    filtered = [i for i in range(1, n + 1) if i not in powers_as_set]
    other_numbers = filtered[:n - MAX_POWER_OF_2]

    print(" ".join(map(str, powers)), end=" ")
    print(" ".join(map(str, other_numbers)))

    # Receive set of numbers
    other_numbers.extend(map(int, input().split()))

    # Keep difference among sum of A and B close (< 10**9)
    a, b = set(), set()
    fill_sets(other_numbers, a, b)
    # Use powers to fill the gap
    fill_sets(powers[::-1], a, b)

    print(" ".join(map(str, a)))
