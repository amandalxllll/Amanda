"""
Question 1:

Write a function that prompts the user for a weight on earth and prints the equivalent weight on the moon (16.5%)

Weight on Moon = weight on Earth * 0.165

Notice:
1. Please write pseudo-code before coding the function.
2. Your function should include docstring.
3. Write your own test code, i.e. call the function.
"""

def moon_weight(earth_weight):
    """
    return your weight on the moon
    step 1: input earth weight
    step 2: calculate earth weight *0.165 
    step 3: return moon_weight
    """
    moon_weight = earth_weight *0.165

    return moon_weight()

"""
Question 2:

Write a function that takes two arguments - 1. weight on earth (float), 2. planet (str) - and returns the equivalent weight on that planet. We assume Moon is a planet although it is not.

Weight on Moon = weight on Earth * 0.165
Weight on Mars = weight on Earth * 0.378
Weight on Venus = weight on Earth * 0.904

Notice:
1. You don't have to write pseudo-code before coding the function. However if pseudocode is provided, you will get partial credits even if you Python code is not working.
2. Your function should include docstring.
3. Write your own test code, i.e. call the function.
"""

earthweight1 = input("please enter your weight on earth >>")
earthweight = float(earthweight1)

planet = str(input("please enter your preferred planet>>"))
def weight(earthweight,planet):
    
