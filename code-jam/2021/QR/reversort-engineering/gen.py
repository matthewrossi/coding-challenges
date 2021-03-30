import sys

n = int(sys.argv[1])
print((n + 1) * n // 2)
for i in range((n + 1) * n // 2):
    print(n, i + 1)
