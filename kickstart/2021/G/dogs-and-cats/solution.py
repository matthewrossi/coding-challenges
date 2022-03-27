#!/usr/bin/env python3

def are_there_no_other_dogs(pos):
    for i in range(pos + 1, n):
        if line[i] == 'D':
            return False
    return True


def are_all_dogs_served(n, dog_food, cat_food, additional_cat_food, line):
    for i in range(n):
        pet = line[i]
        if pet == 'D':
            if dog_food == 0:
                return False
            dog_food -= 1
            cat_food += additional_cat_food
        else:
            if cat_food == 0:
                return are_there_no_other_dogs(i)
            cat_food -= 1
    return True

tests = int(input())
for current_test in range(1, tests + 1):
    n, dog_food, cat_food, additional_cat_food = map(int, input().split())
    line = input()
    all_dogs_served = are_all_dogs_served(n, dog_food, cat_food,
                                          additional_cat_food, line)
    result = "YES" if all_dogs_served else "NO"
    print("Case #{}: {}".format(current_test, result))
