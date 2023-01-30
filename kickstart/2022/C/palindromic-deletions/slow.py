#!/usr/bin/env python3

import math

MODULO = 10**9 + 7


def is_palindrome(string):
    n = len(string)
    for i in range(n // 2):
        if string[i] != string[n - i - 1]:
            return False
    return True


# def count_palindromes(string, count):
#     global palindromes

#     if not string:
#         palindromes += count

#     for i in range(len(string)):
#         new_string = string[:i] + string[i + 1:]
#         count_palindromes(new_string, count + is_palindrome(new_string))


# TODO: Try implementing it with the stack https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


nof_tests = int(input())
for test in range(1, nof_tests + 1):
    n = int(input())
    s = input()
   
    # palindromes = 0
    # count_palindromes(s, 0)

    palindromes = 0
    stack = [(s, 0)]
    while stack:
        current_string, count = stack.pop()

        if not current_string:
            palindromes += count
        
        for i in range(len(current_string)):
            next_string = current_string[:i] + current_string[i + 1:]
            stack.append((next_string, count + is_palindrome(next_string)))
    
    combinations = math.factorial(len(s))

    # Compute result by using the modular moltiplicative inverse
    # Hack when you don't know the modular moltiplicative inverse even exists
    # i = 0
    # while (MODULO * i + palindromes) % combinations:
    #     i += 1
    # result = (MODULO * i + palindromes) // combinations
    # Extended Euclidean algorithm (Python 3.7 and earlier)
    result = (palindromes * modinv(combinations, MODULO)) % MODULO
    # Using built-in function (Python 3.8+)
    # result = (candies * pow(combinations, -1, MODULO)) % MODULO

    print("Case #{}: {}".format(test, result))
