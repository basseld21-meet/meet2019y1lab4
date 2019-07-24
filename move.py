import turtle
finn=turtle.Turtle()
finn.penup
finn.left(90)
finn.shape('turtle')

def up():
    finn.forward(50)

def down():
    finn.backward(50)

def right():
    finn.right(90)

def left():
    finn.left(90)
    
turtle.onkeypress(up, 'w')

turtle.onkeypress(down, 's')

turtle.onkeypress(right, 'd')

turtle.onkeypress(left, 'a')









turtle.listen()

turtle.mainloop()
