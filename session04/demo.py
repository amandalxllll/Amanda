import math
print (math.pi)
print (math.sqrt(85))

print('I\'m\"ok\".')

a = 10
if a % 2 == 1 :
    print ("odd")
elif a%2 !=1:
    print ('even')

#age=22
age = int (input ("how old are you? >>"))


if age >= 21:
    print ('Yes, you can.')
else:
    print('Sorry, you cannot.')

#22 and USA
age = int (input ("how old are you? >>"))
country = input ('Which country are you in?')


if age >= 21 or country. lower() not in ['usa','us','united states']:
    print ('Yes, you can.')
else:
    print('Sorry, you cannot.')