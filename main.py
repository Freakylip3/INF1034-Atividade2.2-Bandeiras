from turtle import *
from time import sleep
t =  Turtle()
t.speed(2)

#bamdeira itália

def Bandeira1():
    t.pu()
    t.goto(0, 0)
    t.pd()
    t.fillcolor('blue')
    t.begin_fill()
    for _ in range(2):
        t.lt(90)
        t.fd(100)
        t.lt(90)
        t.fd(400)
    t.end_fill()
    t.fillcolor('white')
    t.begin_fill()
    t.lt(90)
    t.fd(200)
    t.lt(90)
    t.fd(400)
    t.lt(90)
    t.fd(100)
    t.lt(90)
    t.fd(400)
    t.end_fill()
    t.fillcolor('red')
    t.begin_fill()
    t.lt(90)
    t.fd(200)
    t.lt(90)
    t.fd(400)
    t.lt(90)
    t.fd(100)
    t.lt(90)
    t.fd(400)
    t.end_fill()
    sleep(5)

#bandeira Colombia
 
def Bandeira2():
    t.pu()
    t.goto(0, 0)
    t.pd()
    t.fillcolor('red')
    t.begin_fill()
    for _ in range(2):
        t.lt(90)
        t.fd(100)
        t.lt(90)
        t.fd(400)
    t.end_fill()
    t.fillcolor('blue')
    t.begin_fill()
    t.lt(90)
    t.fd(200)
    t.lt(90)
    t.fd(400)
    t.lt(90)
    t.fd(100)
    t.lt(90)
    t.fd(400)
    t.end_fill()
    t.fillcolor('yellow')
    t.begin_fill()
    t.lt(90)
    t.fd(200)
    t.lt(90)
    t.fd(400)
    t.lt(90)
    t.fd(100)
    t.lt(90)
    t.fd(400)
    t.end_fill()
    sleep(5)


    


    
print(Bandeira1())
print(Bandeira2())










mainloop()
