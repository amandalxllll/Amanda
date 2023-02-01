#Exercise 3
def my_abs_3(n):
    """
    print the absolute value of given number
    """
    if n<0:
        print(-n)
    else:
        print(n)

my_abs_3(-2)
my_abs_3(0)
my_abs_3(3)

#Exercise 4
def my_abs_4(n):
    """
    return the absolute value of given number
    """
    if n<0:
       return(-n)
    else:
        return (n)

print (my_abs_4(-2))

#import math
#print(math.sqrt(my_abs_4(-4)))

#Exercise 5
a=5
def my_abs_5 (n):
    """
    first allow integers and float, then return absolute value of given number
    """
    if isinstance(n,(int,float)):
        if n<0:
            return -n
        else:
            return n
    else: print("The input type is not correct")

print(my_abs_5(a))
