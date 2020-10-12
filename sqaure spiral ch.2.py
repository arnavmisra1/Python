# square spiral
import turtle
colors = ['red', 'blue', 'green' , 'black']
t = turtle.Pen()
t.speed(0)
for x in range(100):
    t.pencolor(colors[x%4])
    t.width(x/100+1)
    t.forward(x)
    t.left(90)
    
