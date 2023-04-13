class Point:
    """Represents a point in 2-D space.

    attributes: x, y
    """
p1 = Point() #creating an object of type Point
print(type(p1))

p1.x = 3
p1.y = 4
#print (p1.x,p1.y)

class Human:
    """
    attributes: name, age, 
    """
    def __init__(self,name,age):
        self.name =name
        self.age = age

    def __str__(self):
        return f'Name:{self.name},Age:{self.age,},Weight"{self.weight}'


# kydell = Human () #creating an instance of Human type
# kydell.name = 'Keydell'
# kydell.age = 22

# john = Human()
# john.name = 'John'
# john.age = 21
kydell = Human('Keydall',22)
john = Human("John",21)

print(kydell.name)