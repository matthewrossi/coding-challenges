import itertools


def has_palindrome_substring(string):
    for pos in range(len(string)):
        if longest_palindrome_in(string, pos) > 5:
            return True    
    return False


def longest_palindrome_in(string, center): 
    left = right = center
    while left >= 0 and right < len(string) and string[left] == string[right]:
        left -= 1
        right += 1

    return (right - left) / 2


def has_palindrome_substring(string):
    return longest_palindrome(string) > 5


def longest_palindrome(string):
    """Manacher's algorithm"""
    n = len(string)
    p = [0] * n

    left, right = 0, -1
    for i in range(n):
        k = 0 if i > right else min(p[left + right - i], right - i)
        while i - k  >= 0 and i + k < n and string[i - k] == string[i + k]:
            k += 1
        p[i] = k
        if i + k > right:
            left = i - k
            right = i + k

    return max(p)


nof_tests = int(input())
for test in range(1, nof_tests + 1):
    length = int(input())
    string = input()

    # Rewrite string with sep chars
    string = "|".join(['', *list(string), ''])
    # Find question marks positions
    qmarks = [i for i in range(len(string)) if string[i] == '?']

    if not qmarks:
        is_impossible = has_palindrome_substring(string)
    else:
        # Try all possible question mark initializations
        is_impossible = True
        for values in itertools.product([0, 1], repeat=len(qmarks)):
            # Initialize question marks
            pieces = [string[:qmarks[0]]]
            for i in range(len(qmarks)):
                pieces.append(str(values[i]))
                end = qmarks[i + 1] if i + 1 < len(qmarks) else len(string)
                pieces.append(string[qmarks[i] + 1:end])
            current_string = "".join(pieces)

            if not has_palindrome_substring(current_string):
                is_impossible = False
                break

    solution = "IMPOSSIBLE" if is_impossible else "POSSIBLE"
    print("Case #{}: {}".format(test, solution))