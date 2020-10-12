import turtle
colors  = ['red', 'blue', 'green', 'black']
t = turtle.Pen()
t.speed(0)
for x in range(100):
    t.width(x/100+1)
    t.pencolor(colors[x%4])
    t.circle(2*x)
    t.left(60)
