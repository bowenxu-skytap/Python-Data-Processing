
def prove37():
    for i in range(37*3, 1000, 37):
        hundred = i // 100
        ten = i % 100 // 10
        one = i % 100 % 10
        num1 = ten * 100 + one * 10 + hundred
        num2 = one * 100 + hundred * 10 + ten
        if(num1 % 37 != 0 or num2 % 37 != 0):
            return False
    return True

print(prove37()) 