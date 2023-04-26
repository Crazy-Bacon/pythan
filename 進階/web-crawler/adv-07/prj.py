from ttkbootstrap import *
import sys
import os

os.chdir(sys.path[0])


def on_switch_change():
    c_label.config(text=str(c.get()))


e = 20
a = tk.Tk()
a.title("My GUI")
a.option_add("*font", ("Helvetica", e))
s = Style(theme="vapor")
s.configure('my.TButton', font=('Helvetica', e))
c = BooleanVar()
c.set(True)

c_label = Label(a, text="True")
c_label.grid(row=1, column=2)

g = Checkbutton(a,
                variable=c,
                onvalue=True,
                offvalue=False,
                command=on_switch_change)
g.grid(row=1, column=1)
r_label = Label(a, text="")
r_label.grid(row=1, column=2)

a.mainloop()