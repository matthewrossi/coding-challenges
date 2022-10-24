#!/usr/bin/env python3

HAND_POSITIONS = {
    "start": ["/", "\\"],
    "hip": ["<", ">"],
    "head": ["(", ")"]
}
LEG_POSITIONS = {
    "in": ["<", ">"],
    "out": ["/", "\\"]
}

MIRROR = {
    "/": "\\",
    "\\": "/",
    "<": ">",
    ">": "<",
    "(": ")",
    ")": "("
}

class Dancer:
    def __init__(self):
        self.side = ["right", "left"]
        self.hands = ["/", "\\"]
        self.legs = ["/", "\\"]

    def __str__(self):
        tokens = []
        # Head level
        h0 = ' ' if self.hands[0] != '(' else '('
        h1 = ' ' if self.hands[1] != ')' else ')'
        tokens.append(f"{h0}o{h1}")
        # Body level
        h0 = self.hands[0] if self.hands[0] != '(' else ' '
        h1 = self.hands[1] if self.hands[1] != ')' else ' '
        tokens.append(f"{h0}|{h1}")
        # Leg level
        tokens.append(f"{self.legs[0]} {self.legs[1]}")
        return "\n".join(tokens)


    def turn(self):
        self.side.reverse()
        self.hands.reverse()
        self.legs.reverse()

        self.hands = [MIRROR[limb] for limb in self.hands]
        self.legs = [MIRROR[limb] for limb in self.legs]

def main():
    nof_tests = int(input())
    for _ in range(nof_tests):
        curr_dancer = Dancer()

        nof_commands = int(input())
        for _ in range(nof_commands):
            tokens = input().split()

            # Say
            if tokens[0] == "say":
                print(*tokens[1:])
                continue
            
            # Turn
            if tokens[0] == "turn":
                curr_dancer.turn()
            else:
                side = curr_dancer.side.index(tokens[0])
                if tokens[1] == "hand":
                    curr_dancer.hands[side] = HAND_POSITIONS[tokens[3]][side]
                else:   # leg
                    curr_dancer.legs[side] = LEG_POSITIONS[tokens[2]][side]
            print(curr_dancer)       


if __name__ == "__main__":
    main()
