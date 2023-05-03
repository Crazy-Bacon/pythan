from ttkbootstrap import *
import sys
import os
import requests

os.chdir(sys.path[0])


def jj():
    global t
    if c.get() == True:
        t = (t - 32) * 5 / 9
        f_label.config(text=f"溫度:{t}°C")
    else:
        t = t * (9 / 5) + 32
        f_label.config(text=f"溫度:{t}°F")


def hi():
    global t
    api_Key = "892da2f13edf3c7f382637760e72d224"
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    city_name = entry.get()
    units = "metric"
    lang = "zh_tw"
    send_url = base_url
    send_url += "appid=" + api_Key
    send_url += "&q=" + city_name
    send_url += "&units=" + units
    send_url += "&lang=" + lang
    print(send_url)
    response = requests.get(send_url)
    info = response.json()
    print(info)
    print(info["main"]["temp"])
    print(info["name"])
    print(info["weather"][0]["description"])
    if "main" in info.keys():
        icon_code = info["weather"][0]["icon"]
        icon_url = f"https://openweathermap.org/img/wn/{icon_code}@2x.png"
        response = requests.get(icon_url)
        with open(f"{icon_code}.png", "wb") as icon_file:
            icon_file.write(response.content)

        f_label.config(text=f'溫度:{info["main"]["temp"]}°C')
        i_label.config(text=f'描述:{info["weather"][0]["description"]}')
        t = info["main"]["temp"]
        image = Image.open(f"{icon_code}.png")
        tk_imagr = ImageTk.PhotoImage(image)
        d_label.config(image=tk_imagr)
        d_label.image = tk_imagr
    else:
        print(" CZity Not Found")


def on_switch_change():
    info["main"]["temp"]


e = 20
a = tk.Tk()
a.title("My GUI")
a.option_add("*font", ("Helvetica", e))
s = Style(theme="vapor")
s.configure('my.TButton', font=('Helvetica', e))
s.configure('my.TCheckbutton', font=('Helvetica', e))

c_label = Label(a, text="請輸入想搜尋的城市:")
c_label.grid(row=0, column=0)

b = Button(a, text="獲得天氣資訊", style='my.TButton', command=hi)
b.grid(row=0, column=2)

entry = Entry(a, width=30)
entry.grid(row=0, column=1, padx=10, pady=10)

d_label = Label(a, text="天氣圖標")
d_label.grid(row=1, column=0)

f_label = Label(a, text="溫度:")
f_label.grid(row=1, column=1)

i_label = Label(a, text="描述:")
i_label.grid(row=1, column=2)

c = BooleanVar()
c.set(True)
g = Checkbutton(a,
                text='溫度單位(°C/°F)',
                variable=c,
                onvalue=True,
                offvalue=False,
                command=jj,
                style='my.TCheckbutton')
g.grid(row=2, column=1)

a.mainloop()