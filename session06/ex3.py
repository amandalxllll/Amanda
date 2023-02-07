#Exercise 3.1
import turtle
leo = turtle.Turtle()

for i in range(60):
    
    leo.fd(100)
    leo.lt(90)
    leo.fd(100)
    leo.lt(90)
    leo.fd(100)
    leo.lt(90)
    leo.fd(100)
    leo.lt(90)
    leo.lt(5)

turtle.mainloop()

#Exercise 3.2

for i in range(30):
    
    leo.fd(100)
    leo.lt(90)
    leo.fd(100)
    leo.lt(90)
    leo.fd(100)
    leo.lt(90)
    leo.fd(100)
    leo.lt(90)
    leo.lt(5)


#Ecercise 3.3
def triangle_60(t):
    for i in range (60):
       
        turtle.fd(100)
        turtle.rt(30)
        turtle.fd(60)
        turtle.rt(60)


turtle.mainloop()