#!/usr/bin/env python3

from curses.ascii import isalpha
def decrypt(c):
    if not c.isalpha():
        return c
    
    base = 'A' if c.isupper() else 'a'
    return chr(ord(base) + (ord(c) - ord(base) - 12) % 26)


def main():
    str = input()
    res = [decrypt(c) for c in str]
    print("".join(res))


if __name__ == "__main__":
    main()