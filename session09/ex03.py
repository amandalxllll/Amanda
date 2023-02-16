from ast import main
import math


epsilon = 0.0000001
def test_square_rppt (x,n):
    while True:
        print (x)
        a = (x + n /x )/2
        if abs (a-x)<epsilon:
            break
        x=a
    return x, test_square_rppt,math.sqrt(x), math.sqrt(x)-float(test_square_rppt)

if __name__ == "__main__":
    main()