from ttkbootstrap import *
from tkinter import filedialog
import sys
import os

os.chdir(sys.path[0])


def show_result():
    entry_text = entry.get()
    ans = eval(entry_text)
    label.config(text=ans)


e = 20
a = tk.Tk()
a.title("My GUI")
a.option_add("*font", ("Helvetica", e))
s = Style(theme="vapor")
s.configure('my.TButton', font=('Helvetica', e))
entry = Entry(a, width=30)
entry.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
button = Button(a, text="顯示計算結果", command=show_result, style="my.TButton")
button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
label = Label(a, text="計算結果")
label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
a.mainloop()
