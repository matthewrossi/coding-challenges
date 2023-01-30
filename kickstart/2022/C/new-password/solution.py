#!/usr/bin/env python3

nof_tests = int(input())
for test in range(1, nof_tests + 1):
    n = int(input())
    psw = input()

    has_uppercase = has_lowercase = has_digit = has_special_char = False
    for c in psw:
        if 'A' <= c <= 'Z':
            has_uppercase = True
        elif 'a' <= c <= 'z':
            has_lowercase = True
        elif '0' <= c <= '9':
            has_digit = True
        elif c == '#' or c == '@' or c == '*' or c == '&':
            has_special_char = True

    res = [psw]
    if not has_uppercase:
        res.append('A')
    if not has_lowercase:
        res.append('a')
    if not has_digit:
        res.append('0')
    if not has_special_char:
        res.append('#')
    
    to_add = 7 - len("".join(res))
    for _ in range(to_add):
        res.append("a")

    print("Case #{}: {}".format(test, "".join(res)))
