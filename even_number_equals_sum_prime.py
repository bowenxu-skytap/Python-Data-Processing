from math import sqrt

def isprime(i):
    if i == 1:
        return False
    k = int(sqrt(i))
    for j in range(2, k+1):
        if i % j == 0:
            return False
    return True

p = []
for i in range(2, 2000):
    if isprime(i):
        p.append(i)

count = 0
for i in range(4, 201, 2):
    flag = 0
    for k in p:
        if flag == 1:
            break
        for v in p:
            if i == k + v:
                print(i, "=", k, "+", v, end=' ')
                flag = 1
                break
    count += 1
    if count == 4:
        count = 0
        print('\n')
                
