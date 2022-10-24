#!/usr/bin/env python3

# Solution with spaces only at the end

NOF_WHEELS = 8
WHEEL_SIZE = 10

def main():
    min_word_length = NOF_WHEELS
    counts = [{} for _ in range(NOF_WHEELS)]
    try:
        while word := input():
            min_word_length = min(min_word_length, len(word))
            for wheel, c in enumerate(word[:-1]):
                counts[wheel][c] = counts[wheel].get(c, 0) + 1
    except:
        pass

    # For each wheel keep the top 9 lower case letters
    wheels = []
    for wheel in range(NOF_WHEELS):
        count = counts[wheel]
        keys = list(count.keys())
        values = list(count.values())
        idx = sorted(range(len(values)), key=lambda i: values[i], reverse=True)

        best_keys = [keys[idx[i]] for i in range(WHEEL_SIZE)]
        wheels.append(best_keys)

    for i, wheel in enumerate(wheels):
        if i >= min_word_length:
            wheel[-1] = ' '
        print("".join(wheel))


if __name__ == "__main__":
    # main()
    print("scpabmtrdf")
    print("aeoirulhnt")
    print("ranteilso")
    print("eitanlsrd")
    print("eistrnalo")
    print("ensritadl")
    print("esntrgdal")
    print("sedgynrtl")
