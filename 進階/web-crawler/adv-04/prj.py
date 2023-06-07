from ttkbootstrap import *
from tkinter import filedialog
import sys
import os

os.chdir(sys.path[0])


def test():
    print("text")


def open_file():
    global file_path
    file_path = filedialog.askopenfilename(initialdir=sys.path[0])
    label2.config(text=file_path)


def show_imge():
    global file_path
    image = Image.open(file_path)
    image = image.resize((canvas.winfo_width(), canvas.winfo_height()),
                         Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, anchor='nw', image=photo)
    canvas.image = photo


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
button = Button(a, text="瀏覽", command=open_file, style="my.TButton")
button.grid(row=0, column=2, sticky="w")
button2 = Button(a, text="顯示", command=show_imge, style="my.TButton")
button2.grid(row=1, column=0, columnspan=3, sticky="EW")
canvas = Canvas(a, width=600, height=600)
canvas.grid(row=2, column=0, columnspan=3, sticky="EW")

a.mainloop()
