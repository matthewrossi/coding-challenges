MIN_LEN = 5


def is_palindrome(string):
    for i in range(len(string) // 2):
        if string[i] != string[len(string) - i - 1]:
            return False
    return True
    

def has_palindrome_substring(string):
    if len(string) < MIN_LEN:
        return False

    prefixes = [""]
    for i in range(len(string)):
        next_prefixes = []
        # Update prefixes with next char if not palindrome
        for prefix in prefixes:
            if string[i] == '?':
                tmp_prefixes = [prefix + '0', prefix + '1']
            else:
                tmp_prefixes = [prefix + string[i]]
            for tmp_prefix in tmp_prefixes:
                if i < MIN_LEN or not is_palindrome(tmp_prefix):
                    next_prefix = tmp_prefix if i < MIN_LEN else tmp_prefix[1:]
                    if i < MIN_LEN - 1 or not is_palindrome(next_prefix):
                        next_prefixes.append(next_prefix)

        # No prefixes without palindrome
        if not next_prefixes:
            return True

        prefixes = next_prefixes

    return False


nof_tests = int(input())
for test in range(1, nof_tests + 1):
    length = int(input())
    string = input()

    solution = "IMPOSSIBLE" if has_palindrome_substring(string) else "POSSIBLE"
    print("Case #{}: {}".format(test, solution))
