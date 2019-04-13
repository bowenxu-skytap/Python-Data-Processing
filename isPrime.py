import math

def isPrime(num):
    if num <= 0:
        return False
    if num > 2 and num % 2 == 0:
        return False
    for x in range(3, int(math.sqrt(num)) + 1, 2):
        if num % x == 0:
            return False
    return True


print(isPrime(5))
