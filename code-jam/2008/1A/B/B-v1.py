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

    servings = 1
    pos = [0] * nof_ingredients
    new_kit_may_exist = True
    while new_kit_may_exist:
        new_kit = True
        ingredient = 0
        while new_kit_may_exist and ingredient < nof_ingredients:

            package_changed = True
            while package_changed:
                if pos[ingredient] >= nof_packages:
                    package_changed = False
                    new_kit = False
                    new_kit_may_exist = False
                elif len(servings_per_package[ingredient][pos[ingredient]]) == 0 or \
                        servings_per_package[ingredient][pos[ingredient]][-1] < servings:
                    new_kit = False
                    pos[ingredient] += 1
                else:
                    package_changed = False

            if new_kit_may_exist:
                if len(servings_per_package[ingredient][pos[ingredient]]) > 0 and \
                        servings_per_package[ingredient][pos[ingredient]][0] > servings:
                    new_kit = False
                    servings = servings_per_package[ingredient][pos[ingredient]][0]

            ingredient += 1

        if new_kit:
            kits += 1
            for ingredient in range(nof_ingredients):
                pos[ingredient] += 1

    print("Case #{}: {}".format(case, kits))
