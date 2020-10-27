def remove_starting_zeroes(string):
    start = True
    i = 0
    while i < len(string):
        if start and string[i] == '0' and i + 1 < len(string) and string[i+1] != '+' and string[i+1] != '-':
                string = string[:i] + string[i+1:]
        elif string[i] == '+' or string[i] == '-':
            start = True
            i += 1
        else:
            start = False
            i += 1
    return string


def brute_force(string, pos):
    if pos == len(string):
        number = eval(remove_starting_zeroes(string))
        if number % 2 == 0 or number % 3 == 0 or number % 5 == 0 or number % 7 == 0:
            return 1
        return 0
    return brute_force(string, pos+1) + brute_force(string[:pos] + '+' + string[pos:], pos+2) + brute_force(string[:pos] + '-' + string[pos:], pos+2)


nof_cases = int(input())
for case in range(1, nof_cases+1):
    string = input()
    nof_ugly_numbers = brute_force(string, 1)
    print("Case #{}: {}".format(case, nof_ugly_numbers))
