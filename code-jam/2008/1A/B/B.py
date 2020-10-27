import sys

def build_kit(starting_package):
    for servings in starting_package:
        kit = [starting_package]
        for ingredient in range(1, nof_ingredients):
            # get the packages that match with the previously chosen package
            matching_packages = []
            for package in range(len(servings_per_package[ingredient])):
                if servings in servings_per_package[ingredient][package]:
                    matching_packages.append(servings_per_package[ingredient][package])
            nof_matching_packages = len(matching_packages)
            if nof_matching_packages > 0:
                kit.append(matching_packages[0])
            else:
                break
        if len(kit) == nof_ingredients:
            return kit
    return []

nof_cases = int(input())
for case in range(1, nof_cases+1):
    nof_ingredients, nof_packages = [int(s) for s in input().split(" ")]
    recipe = [int(s) for s in input().split(" ")]
    quantity_per_package = [[0 for p in range(nof_packages)] for i in range(nof_ingredients)]
    for ingredient in range(nof_ingredients):
        quantity_per_package[ingredient] = [int(s) for s in input().split(" ")]

    # each kit is built with one package per ingredient
    # for each package say how many servings can be done with it considering the [90, 110]% tollerance
    servings_per_package = [[[] for p in range(nof_packages)] for i in range(nof_ingredients)]
    for ingredient in range(nof_ingredients):
        one_serving = recipe[ingredient]
        for package in range(nof_packages):

            nof_possible_servings = int(quantity_per_package[ingredient][package] / one_serving)

            dec = 1
            while 0.9 * one_serving * (nof_possible_servings-dec) <= quantity_per_package[ingredient][package] \
                    <= 1.1 * one_serving * (nof_possible_servings-dec):
                servings_per_package[ingredient][package].insert(0, nof_possible_servings-dec)
                dec += 1

            if 0.9 * one_serving * (nof_possible_servings) <= quantity_per_package[ingredient][package] \
                    <= 1.1 * one_serving * (nof_possible_servings):
                servings_per_package[ingredient][package].append(nof_possible_servings)

            inc = 1
            while 0.9 * one_serving * (nof_possible_servings+inc) <= quantity_per_package[ingredient][package] \
                    <= 1.1 * one_serving * (nof_possible_servings+inc):
                servings_per_package[ingredient][package].append(nof_possible_servings+inc)
                inc += 1

    # combine the sets to build up kits
    kits = 0
    # sort for each ingredient all the packages
    for ingredient in range(nof_ingredients):
        servings_per_package[ingredient].sort()
    starting_packages = servings_per_package[0]

    while len(starting_packages) > 0:
        starting_package = starting_packages[0]
        kit = build_kit(starting_package)
        if len(kit) == 0:
            # no kit can be built with this package
            del starting_packages[0]
        else:
            # a kit has been built with this package, so remove all the packages that are part of it
            for ingredient, package in enumerate(kit):
                servings_per_package[ingredient].remove(package)
            kits += 1

    print("Case #{}: {}".format(case, kits))
