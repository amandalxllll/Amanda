""""
I want to create a python program which describe my family tree for my family research. There are around 50
figures that I can think of and I do not want to use excel or words to draw relationship between each of them.
"""

class Family:
    """
    attributes: name, age, 
    """
    def __init__(self,name,age,gender,relationship):
        self.name =name
        self.age = age
        self.gender = gender
        self.relationship = relationship
    def __str__(self):
        return f'name = {self.name}, age = {self.age},gender={self.gender}, relationship={self.relationship}'
"""
you can just type the information of your family here, for example, if David if the grandpa ages 81, you can type
"""
David = Family("David",90,"male","grandpa")
print(David)

    