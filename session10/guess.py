import random

name = input("Hello! What's your name>>")

number = int(random.randint(1, 50))

print("Well,", name, ", I am thinking of a number between 1 and 50.")


def guess():
    for i in range(1, 7):
        guess1 = input("Take a guess>>>")
        guessnumber = int(guess1)
        if number == guessnumber:
            print("Good job,", name, "! You guessed my number in", i, "guess")
            break
        elif number >= guessnumber:
            print(f"Higher! You have {6-i} chance")
        else:
            print(f"Lower, you have {6-i} chance")


print(guess())
print("the right answer is", number)
