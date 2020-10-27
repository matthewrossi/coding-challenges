"""
at 1 + 10 * i something happens
something is one of:
- complement array             25%
- reverse array                25%
- complement and reverse array 25%
- nothing                      25%
answer reflects latest state

input/output
up to 150 queries
program asks for value of B[idx] by sending idx
judge response with the value B[idx] either 0 or 1 character
program outputs a string of B characters, representing the current state of the array
judge responds Y/N, if N no other interaction
"""

import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
    sys.stderr.flush()

MAX_QUERIES = 150

def dummy():
    print(1)
    sys.stdout.flush()
    input()

def recognize_and_adapt(bits, eq, neq):
    if eq == -1:
        # different
        print(neq + 1)
        sys.stdout.flush()
        if bits[neq] != bool(int(input())):
            bits.reverse()
        dummy()
    elif neq == -1:
        # equal
        print(eq + 1)
        sys.stdout.flush()
        if bits[eq] != bool(int(input())):
            bits[:] = [not bit for bit in bits]
        dummy()
    else:
        # both
        print(eq + 1)
        print(neq + 1)
        sys.stdout.flush()
        eq_response = bool(int(input()))
        neq_response = bool(int(input()))
        if bits[eq] == eq_response:
            if bits[neq] != neq_response:
                bits.reverse()
        else:
            if bits[neq] != neq_response:
                bits[:] = [not bit for bit in bits]
            else:
                bits.reverse()
                bits[:] = [not bit for bit in bits]


nof_tests, nof_bits = map(int, input().split())
for i in range(1, nof_tests + 1):
    bits = [False] * nof_bits

    num = 0
    eq = neq = -1
    for idx in range(int(nof_bits / 2)):
        if num and not num % 10:
            recognize_and_adapt(bits, eq, neq)
            num += 2

        print(idx + 1)
        print(nof_bits - idx)
        sys.stdout.flush()
        bits[idx] = bool(int(input()))
        bits[nof_bits - idx - 1] = bool(int(input()))
        if eq == -1 and bits[idx] == bits[nof_bits - idx -1]:
            eq = idx
        if neq == -1 and bits[idx] != bits[nof_bits - idx -1]:
            neq = idx
        num += 2
    else:
        if num and not num % 10:
            recognize_and_adapt(bits, eq, neq)
            num += 2

    bits = list(map(int, bits)) # 0/1
    print("".join(map(str, bits)))
    sys.stdout.flush

    verdict = input()
    if verdict != 'Y':
        break
