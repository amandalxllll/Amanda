from cmath import sqrt
import math

a=float(input("Please enter a>>>"))
b=float(input("Please enter b>>>"))
c=float(input("Please enter c>>>"))

def quadratic(a,b,c):
    """
    Solve quadratic equation
    """
    R1 = (-1 * b + sqrt(b**2-4*a*c))/2*a
    R2=  (-1 * b - sqrt(b**2-4*a*c))/2*a
    return R1,R2

print(f'"The result is",{quadratic(a,b,c)}') #I tried to add 8.3f, but it says typeerrors