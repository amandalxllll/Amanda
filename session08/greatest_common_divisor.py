x = int(input("please input x >>"))
y = int(input("please input y>>"))

def greatest_common_divisor (x,y):
    if x > y:
        r = y
    else:
        r = x
    for i in range (1, r+1):
        if (x % i == 0) and (y % i ==0):
            greatest_common_divisor=i
    return greatest_common_divisor

print(greatest_common_divisor(x,y))