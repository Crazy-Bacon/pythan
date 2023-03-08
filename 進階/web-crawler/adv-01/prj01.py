from tkinter import *


def hi_fun():
    global change
    print("Hellow ...")
    if change == False:
        display.config(text="Hellow ...", fg="#75FFFF", bg="#FF00BE")
    else:
        display.config(text="Hellow ...", fg="", bg="")
    change = not (change)


change = False
win = Tk()  #召喚視窗
win.title("My first GUT")  #新增標題
btn = Button(win, text="Click me", command=hi_fun, fg="#75FFFF",
             bg="#FF00BE")  #
btn.pack()  #
display = Label(win, text="hi", fg="#75FFFF", bg="#FF00BE")
display.pack()
win.mainloop()  #無限循環
