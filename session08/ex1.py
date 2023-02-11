a1 = input("Please input number a >>")
b1 = input("Please input number b >>")
c1 = input("Please input number c >>")
n1 = input("Please input number n >>")

a = int(a1)
b = int(b1)
c = int(c1)
n = int(n1)


def check_fermat(a, b, c, n):
    """
    check to see if Fernat's theorem work
    """
    if n <= 2:
        print("Fermat theorem only work when n>2")
    else:
        if a**n + b**n == c**n:
            print("Holy smokes, Fermat was wrong!")
        else:
            print("No, that doesn't work!")
