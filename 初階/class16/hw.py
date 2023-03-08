import turtle as t


def tur(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.forward(100)
    t.left(120)
    t.forward(100)
    t.left(120)
    t.forward(100)
    t.left(120)
    t.forward(25)
    t.right(90)
    t.forward(150)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(150)
    t.done()


x = int(input("x="))
y = int(input("y="))
tur(x, y)
