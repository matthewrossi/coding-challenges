import sys

sys.setrecursionlimit(10**9)

nof_tests = int(input())
for test in range(nof_tests):
    expression = input()
    
    brackets = 0
    for i in range(len(expression)):
        curr_char = expression[i]
        if curr_char == "(":
            if i != 0:
                prev_char = expression[i - 1]
                if prev_char not in "+-*(":
                    print("invalid")
                    break
            if i == len(expression) - 1:
                print("invalid")
                break
            next_char = expression[i + 1]
            if next_char in "+-*)":
                print("invalid")
                break
            brackets += 1
        elif curr_char == ")":
            if i == 0:
                print("invalid")
                break
            prev_char = expression[i - 1]
            if prev_char in "+-*(":
                print("invalid")
                break
            if i != len(expression) - 1:
                next_char = expression[i + 1]
                if next_char not in "+-*)":
                    print("invalid")
                    break
            if brackets == 0:
                print("invalid")
                break
            brackets -= 1
        elif curr_char in "+-*":
            if i == 0 or i == len(expression) - 1:
                print("invalid")
                break
            prev_char = expression[i - 1]
            next_char = expression[i + 1]
            if prev_char in "+-*(" or next_char in "+-*)":
                print("invalid")
                break
    else:
        # We get here only when loop ends without breaks
        if brackets:
            print("invalid")
        else:
            count = 0
            for i in range(len(expression)):
                if expression[i] == "(" and expression[-(i+1)] == ")":
                    count += 1
            print(eval(expression[count:len(expression)-count]) % (10**9 + 7))
