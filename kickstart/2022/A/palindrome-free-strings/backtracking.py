import itertools

MIN_LEN = 5


def is_palindrome(string):
    for i in range(len(string) // 2):
        if string[i] != string[len(string) - i - 1]:
            return False
    return True
    

def has_palindrome_substring(string):
    if len(string) < MIN_LEN:
        return False

    # Init stack according to string prefix
    stack = []
    qmarks = string[:MIN_LEN].count('?')
    for values in itertools.product([0, 1], repeat=qmarks):
        # Init question marks
        pieces = []
        qi = 0
        for i in range(MIN_LEN):
            if string[i] == '?':
                pieces.append(str(values[qi]))
                qi += 1
            else:
                pieces.append(string[i])
        stack.append(("".join(pieces), MIN_LEN))

    # Explore space of solution one character at a time
    while stack:
        state, i = stack.pop()
        
        # Skip state if palindrome
        if is_palindrome(state):
            continue

        # Found a string without palindromes
        if i == len(string):
            return False

        # Add new potential states 
        if string[i] == '?':
            tmp_states = [state + '0', state + '1']
        else:
            tmp_states = [state + string[i]]
        for tmp_state in tmp_states:
            if not is_palindrome(tmp_state):
                stack.append((tmp_state[1:], i + 1))

    return True


nof_tests = int(input())
for test in range(1, nof_tests + 1):
    length = int(input())
    string = input()

    solution = "IMPOSSIBLE" if has_palindrome_substring(string) else "POSSIBLE"
    print("Case #{}: {}".format(test, solution))
