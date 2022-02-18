DISLIKES = {'Y', 'y'}
VOWELS = {'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'}


def has_ruler(kingdom):
    return kingdom[-1] not in DISLIKES


def is_alice(kingdom):
    return kingdom[-1] in VOWELS


def get_ruler(kingdom):
    if not has_ruler(kingdom):
        return "nobody"
    return "Alice" if is_alice(kingdom) else "Bob"


if __name__ == "__main__":
    nof_tests = int(input())
    for test in range(1, nof_tests + 1):
        kingdom = input()
        ruler = get_ruler(kingdom)
        print("Case #{}: {} is ruled by {}.".format(test, kingdom, ruler))
