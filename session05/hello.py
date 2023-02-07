#a = None
#type (a) # would print out as nonetype
#a=""
#type (a) #would print out as str
import math
import random


print(r'It\' ok.')
print("It\'s ok")

#get a random between 0 and 1
random.random ()
#get a random between 0.0 and 1.0
random.random () *10
#get a random integer between 0 an 10 (10 excluded)
int(random.random()*10)
math.floor(random.random()*10)
random.randint(0,9)

# what is the type and the alue of the expression in line 2 below
year=2020
year % 4 ==0 and year % 100 != 0 or year % 400 ==0 # != is not equal
#Boolean and True