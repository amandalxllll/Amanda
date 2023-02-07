import myabs
print ((myabs.my_abs(-100)))
def my_abs(n):
    if n<0:
        return -n
    else:
        return n
print (f"_ _ name_ _:{__name__}")
def main():
    print(my_abs(-2))