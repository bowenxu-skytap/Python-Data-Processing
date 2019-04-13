def hanoi(a,b,c,n):
    if n == 1:
        print(a, '->', c)
    else:
        hanoi(a,c,b,n-1)
        print(a, '->', c)
        hanoi(b,a,c,n-1)
        
hanoi('a', 'b', 'c', 3)