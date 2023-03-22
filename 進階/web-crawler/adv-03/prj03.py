from ttkbootstrap import *
import sys
import os

os.chdir(sys.path[0])


def test():
    print("text")


e = 20
a = tk.Tk()
a.title("My GUI")
a.option_add("*font", ("Helvetica", e))
s = Style(theme="vapor")
s.configure('my.TButton', font=('Helvetica', e))
label = Label(a, text="選擇檔案:")
label.grid(row=0, column=0, sticky="E")
label2 = Label(a, text="無")
label2.grid(row=0, column=1, sticky="E")
button = Button(a, text="瀏覽", command=test, style="my.TButton")
button.grid(row=0, column=2, sticky="w")
button2 = Button(a, text="顯示", command=test, style="my.TButton")
button2.grid(row=1, column=0, columnspan=3, sticky="EW")
canvas = Canvas(a, width=600, height=600)
canvas.grid(row=2, column=0, columnspan=3, sticky="EW")

a.mainloop()
