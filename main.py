from turtle import *
from time import sleep
t =  Turtle()
t.speed(0)

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
    sleep(2)

#bandeira Áustria
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
    sleep(2)


#bandeira Colombia
 
def Bandeira3():
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
    sleep(2)


def Bandeira4():
    t.pu()
    t.goto(-250, 0)
    t.pd()
    t.fillcolor('red')
    t.begin_fill()
    for _ in range (2):
        t.lt(90)
        t.fd(300)
        t.lt(90)
        t.fd(150)
    t.end_fill()
    t.fillcolor('yellow')
    t.begin_fill()
    t.lt(90)
    t.fd(150)
    t.rt(90)
    t.fd(250)
    t.lt(90)
    t.fd(150)
    t.lt(90)       
    t.fd(250)
    t.lt(90)
    t.fd(150)
    t.end_fill()
    t.fillcolor('green')
    t.begin_fill()
    t.fd(150)
    t.lt(90)
    t.fd(250)
    t.lt(90)
    t.fd(150)
    t.lt(90)
    t.fd(250)
    t.end_fill()
    

def EstrelaPreta():
    t.pu()
    t.goto(-180, 0)
    t.fillcolor('black')
    t.begin_fill()
    t.pd()
    for _ in range(5):
        t.goto(-180, 0)
        lt(144)
        fd(45)
    t.end_fill()



        
        
    
    


    
print(Bandeira1())
print(Bandeira2())
print(Bandeira3())
print(Bandeira4())
print(EstrelaPreta())













mainloop()
