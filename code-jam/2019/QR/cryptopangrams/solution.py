from fractions import gcd

def decript(cipher, length):
    primes = set() 
    sequence = []     
    for i in range(length - 1):
        prime = gcd(cipher[i], cipher[i+1])
        primes.add(prime)
        sequence.append(prime)

    # get prime used by the first char
    other_prime = cipher[0] / sequence[0]
    primes.add(other_prime)
    sequence.insert(0, other_prime)
    
    # get prime used by the last char
    other_prime = cipher[length - 1] / sequence[length - 1]
    primes.add(other_prime)
    sequence.append(other_prime)

    primes = list(primes)
    primes.sort()

    key = {}
    base = ord('A')
    for i in range(len(primes)):
        key[primes[i]] = chr(base + i)
    
    plaintext = ""
    for factor in sequence:
        plaintext += key[factor]
    return plaintext


t = int(raw_input())  # read number of tests
for i in xrange(1, t + 1):
    n, l = [int(s) for s in raw_input().split(" ")]   # read primes limit and cipher length
    cipher = [int(s) for s in raw_input().split(" ")] # read cipher
    print "Case #{}: {}".format(i, decript(cipher, l))