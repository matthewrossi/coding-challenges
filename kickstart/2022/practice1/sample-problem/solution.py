def solve(bags, nof_kids):
    nof_candy = sum(bags)
    return nof_candy % nof_kids


if __name__ == "__main__":
    nof_tests = int(input())
    for test in range(1, nof_tests + 1):
        nof_bags, nof_kids = map(int, input().split())
        bags = map(int, input().split())
        res = solve(bags, nof_kids)
        print("Case #{}: {}".format(test, res))
