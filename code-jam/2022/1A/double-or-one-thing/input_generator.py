from operator import length_hint
import random
import string

T = 100
MAX_LENGTH = 10

print(T)
for test in range(T):
    length = random.randint(1, MAX_LENGTH)
    print(''.join(random.choices(string.ascii_uppercase, k=length)))
