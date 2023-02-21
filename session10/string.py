# Exercise 1

prefixes = "JKLMNOPQ"

for letter in prefixes:
    if letter == "O":
        suffix = "uack"
    elif letter == "Q":
        suffix = "uack"
    else:
        suffix = "ack"

    print(letter + suffix)

# Exercise 2
word = "New England Patriots"


def count():
    count = 0
    for letter in word:
        if letter == "a":
            count = count + 1
    return (count)

#Exercise 3 "didnt really get what I should do with this exercise"

def in_both(word1, word2):
    for letter in word1:
        if letter in word2:
            print(letter)

#Exercise 4
print ("the first function trying to make sure a string contains all lowercase letters")
print ("the second function trying to make sure whether letter c is in lowercase")
print("the third function trying to determine if flag is true, use to test c in s")
print ("True")
print ("doing the same thing")

#Exercise 5

def rotate_world (str,int):

        for letter in str:
            x = ord(letter) + int
        if x > 122:
            a = x - 123
            x = 97 + a
            print(chr(x))
        elif x < 97:
            a = 97 - x
            x = 123 - a
            print(chr(x))
        else:
            print(chr(x))