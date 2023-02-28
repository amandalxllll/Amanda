for i in range(10):
    if i % 3 == 0:
        continue
    print(i)

# in-class quiz
"""
Function 1: one simulation, rolling 100 dice
1. creat a variable to stop the sum, initialize it to 0
2. repeat the following step(s) 100 times, simuating rolling one die
    1. get a random integer in range [1,6]
    2. add the randome integer to the sum variable 
3. print the result
Function 2: repeat simulaiton 10 times
1. repeat the following step(s) 10 times (for,while)
    1. call funciton 1
"""
import random


def roll_dice(n=100):
    """
    roll 100 dice and print the sum
    """
    result = 0
    for i in range(n):
        random_number = random.randint(1, 6)
        result += random_number
    avg = result / n
    return result, avg


def repeat_simulation():
    for i in range(10):
        s, mean = roll_dice(100)
        print(f"{s = }, {mean = }")


def main():
    """ """
    repeat_simulation()


if __name__ == "__main__":
    main()
