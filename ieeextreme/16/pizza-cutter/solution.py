#!/usr/bin/env python3

def main():
    nof_tests = int(input())
    for _ in range(nof_tests):
        _, *degrees = [int(token) for token in input().split()]
        cuts = {degree % 180 for degree in degrees}
        print(max(1, 2 * len(cuts)))


if __name__ == "__main__":
    main()