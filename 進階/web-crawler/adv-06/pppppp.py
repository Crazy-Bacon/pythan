from ttkbootstrap import *
from tkinter import filedialog
import sys
import os

e = 20
a = tk.Tk()
a.title("My GUI")
a.option_add("*font", ("Helvetica", e))
s = Style(theme="vapor")
s.configure('my.TButton', font=('Helvetica', e))
c = BooleanVar()
c.set(True)

c_label = Label(e, text="True")
c_label.grid(row=1, column=2)

c = Checkbutton(e,
                variable=c,
                onvalue=True,
                offvalue=False,
                command=on_switch_change)
a.mainloop()