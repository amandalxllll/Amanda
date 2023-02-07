import turtle
leo = turtle.Turtle()
print (leo)

def square(t):
    """
    this function called square that takes a 
    parameter named t, which is a turtle. It should 
    use the turtle to draw a square. Write a function 
    call that passes leo as an argument to square, and 
    then run the program again.
    """
    for i in range(4):
        t.fd(100)
        t.lt(90)

#square(leo)

#Exercise 2.2
def square(t, length):
    """
    use the turt;e to draw a square with side length

    """
square(leo,200)


#Exercise 2.3
def polygon(t,length,n):
    """
    dra an n-sided regular polygon
    """
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

polygon(t=leo,length=50,n=28)

turtle.mainloop()
