from turtle import *
bgcolor("black")
speed(0)
hideturtle()

for i in range(50,400):
    color("red")
    circle(i)
    color("orange")
    circle(i*0.8)
    color("white")
    circle(i*0.6)
    right(3)

done()    
