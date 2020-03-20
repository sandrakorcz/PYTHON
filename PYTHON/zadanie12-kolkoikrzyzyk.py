import turtle
import math

bok=80

def kwadrat():
      for i in range(4):
            turtle.fd(bok)
            turtle.left(90)

def plansza():
      for i in range(3):
            for j in range(3):
                  turtle.pd()
                  kwadrat()
                  turtle.pu()
                  turtle.fd(bok)
            turtle.bk(3*bok)
            turtle.left(90)
            turtle.fd(bok)
            turtle.right(90)
            

def krzyzyk(a,b):
      for i in range(4):
            turtle.rt(45)
            turtle.fd(70)
            turtle.pu()
            turtle.bk(70);
            turtle.pd()
            turtle.rt(45)


       
def kolko(a,b):
      turtle.pu()
      turtle.setx(a*bok+bok/2)
      turtle.sety(b*bok+bok/2-54/math.pi)
      turtle.pd()
      for i in range(36):
            turtle.fd(3)
            turtle.left(10)
      turtle.pu()
