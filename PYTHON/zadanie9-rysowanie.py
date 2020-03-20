import turtle
import random
window=turtle.Screen()
circle=turtle.Turtle()

'''
turtle.circle(150,steps=8)'''

k=["blue","pink","green","yellow","purple"]

for i in range(8):
    turtle.fillcolor(random.choice(k))
    turtle.begin_fill()
    turtle.circle(150,90)
    turtle.end_fill()
    turtle.left(90)
    turtle.fillcolor(random.choice(k))
    turtle.begin_fill()
    turtle.circle(150,90)
    turtle.left(45)
    turtle.end_fill()


