import math


def quadratic(a, b, c):
    """
    Simple version of quadratic equation solver
    a: float
    b: float
    c: float
    Return: two numbers
    """
    discriminant = b**2 - 4 * a * c  # calculate the discriminant

    if discriminant >= 0:  # equation has solutions
        x_1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x_2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return x_1, x_2
    else:
        print('No Real Number Solution.')
        return None


def main():
    a = float(input('please enter a number:'))
    b = float(input('please enter a number:'))
    c = float(input('please enter a number:'))
    sol_1, sol_2 = quadratic(a, b, c)
    if sol_1:
        print(f'The two roots are: {sol_1}, {sol_2}.')
    else:
        print('No Real Number Solution.')


if __name__ == '__main__':
    main()