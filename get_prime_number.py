from math import sqrt

def isprime(i):
    if i == 1:
        return False
    k = int(sqrt(i))
    for j in range(2, k+1):
        if i % j == 0:
            return False
    return True

for i in range(2, 101):
    if isprime(i):
        print(i, end=' ')