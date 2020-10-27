nof_cases = int(input())
for case in range(1, nof_cases+1):
    [nof_lpk, nof_key, nof_letters] = [int(s) for s in input().split(" ")]
    freq = [int(s) for s in input().split(" ")]

    freq.sort(reverse=True)

    keypad_presses = 0
    for letter in range(nof_letters):
        keypad_presses += (letter//nof_key + 1) * freq[letter]

    print("Case #{}: {}".format(case, keypad_presses))
