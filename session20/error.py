try:
    number = float(input('please enter a number:>>'))

    result = 2023/number

    print(result)
except ZeroDivisionError:
    print ('You just entered 0')
except ValueError:
    print ("you should enter an integer")
except:
    print("something wrong happened")
finally:
    print("No matter what happens, we still got here")

print("Hello, world!") # we still want to see this no matter what happen