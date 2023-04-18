class Fractional:
    def __init__(self,a,b):
        self.numerator = a
        self.dominator = b
    def __str__(self):
        """The human readable form"""
        return f'{self.numerator:^3}\n---\n{self.dominator:^3}'
    def __add__(self,other):
        """
        Overload the '+' operator 
        """

frac_1=Fractional(3,2)
frac_2 = Fractional(1,1)
print(frac_1)
print(frac_2)

result = frac_1 +frac_2
print(result)