# factorial

n = input (input("give me a number"))
a =1
for i in range (1,n+1):
    a = a * i
print(f" the factorial of {n} is {a}")

#fibonacci
from cmath import sqrt
import math
g=(1+5**0.5)/2
integer = int(input("your integer is >>>"))
def feb(integer):
    feb = (g ** integer - (1-g)**integer/sqrt(5))
    return feb