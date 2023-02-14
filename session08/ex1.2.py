# Exercuse 2
def calculate_bmi(weight, height):
    """
    return BMI value
    """
    bmi = weight / (height**2)
    return bmi
testcode = calculate_bmi(60,1.71)
print(testcode)



# Exercise 2.1
weight = float(input("please input your weight (in kg)>>"))
height = float(input("please input your height (in m)>>"))

bmi = weight / (height**2)


def calculate_bmi1(weight, height):
    """
    return BMI value and category
    """
    bmi = weight / (height**2)
    if bmi <= 18.5:
        return "Underweight"
    elif 18.5 < bmi < 24.9:
        return "Normal"
    elif 25 < bmi < 29.9:
        return "overweight"
    else:
        return "obseity"


print(bmi)
print(calculate_bmi1(weight, height))
