from tkinter import *
from PIL import Image, ImageTk
import sys
import os


def move_circle(event):
    key = event.keysym
    print(key)
    if key == "Right":
        canvas.move(circle, 10, 0)
    elif key == "Left":
        canvas.move(circle, -10, 0)
    elif key == "Up":
        canvas.move(circle, 0, -10)
    elif key == "Down":
        canvas.move(circle, 0, 10)
    elif key == "d":
        canvas.move(rect, 10, 0)
    elif key == "a":
        canvas.move(rect, -10, 0)
    elif key == "w":
        canvas.move(rect, 0, -10)
    elif key == "s":
        canvas.move(rect, 0, 10)


def exit_fun():
    a.destroy()


os.chdir(sys.path[0])

a = Tk()
a.title("")
quit_bth = Button(a, text="quit", command=exit_fun)
quit_bth.pack()

canvas = Canvas(a, width=400, height=600)
canvas.pack()

a.iconbitmap("crocodile2.ico")
# img = PhotoImage(file="crocodile2.gif")
image = Image.open("1587525807326 - 複製.jpg")
img = ImageTk.PhotoImage(image)
canvas.create_image(100, 100, image=img)
circle = canvas.create_oval(250, 150, 300, 200, fill="red")
rect = canvas.create_rectangle(220, 400, 340, 430, fill="blue")
msg = canvas.create_text(300,
                         100,
                         text="corcodile",
                         fill="black",
                         font=('Arial', 30))
canvas.bind_all('<Key>', move_circle)
a.mainloop()