def mul_digits(num):
    mul = 1
    while num:
        mul *= num % 10
        num //= 10
    return mul


def sum_digits(num):
    sum = 0
    while num:
        sum += num % 10
        num //= 10
    return sum


nof_tests = int(input())
for test in range(1, nof_tests + 1):
    a, b = map(int, input().split())

    solution = 0
    for num in range(a, b + 1):
        if mul_digits(num) % sum_digits(num) == 0:
            solution += 1
    
    print("Case #{}: {}".format(test, solution))