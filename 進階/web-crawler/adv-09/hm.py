from ttkbootstrap import *
import sys
import os
from PIL import Image, ImageTk
import requests
import matplotlib.pyplot as plt
import requests
import datetime
from matplotlib.font_manager import FontProperties
from ttkbootstrap import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

os.chdir(sys.path[0])  # 設定工作目錄


def draw_graph():
    api_Key = "892da2f13edf3c7f382637760e72d224"
    base_url = "https://api.openweathermap.org/data/2.5/onecall?"
    lon = "121.5319"
    lat = "25.0478"
    exclude = "minutely,horuly"
    units = "metric"
    lang = "zh_tw"
    send_url = base_url
    send_url += "lat=" + lat
    send_url += "&lon=" + lon
    send_url += "&exclude=" + exclude
    send_url += "&appid=" + api_Key
    send_url += "&units=" + units
    send_url += "&lang=" + lang
    print(send_url)
    response = requests.get(send_url)
    info = response.json()

    listx = []
    listy = []
    if "daily" in info.keys():
        for i in range(7):
            temp = info["daily"][i]["temp"]["day"]
            time = datetime.fromtimestamp(
                info["daily"][i]["dt"]).strftime("%m/%d")
            print(f"{time}={temp}")
            listx.append(time)
            listy.append(temp)
    else:
        print("fail")


def get_weather_info():
    global units
    api_Key = "892da2f13edf3c7f382637760e72d224"
    base_url = "https://api.openweathermap.org/data/2.5/onecall?"
    exclude = "minutely,horuly"
    units = "metric"
    lang = "zh_tw"
    send_url = base_url
    send_url += "lat=" + lat_entry.get()
    send_url += "&lon=" + lon_entry.get()
    send_url += "&exclude=" + exclude
    send_url += "&appid=" + api_Key
    send_url += "&units=" + units
    send_url += "&lang=" + lang

    response = requests.get(send_url)  # 發送請求，獲得天氣資訊
    info = response.json()  # 將json格式轉換為字典

    listx = []
    listy = []
    if "daily" in info.keys():
        for i in range(7):
            temp = info["daily"][i]["temp"]["day"]
            time = datetime.fromtimestamp(
                info["daily"][i]["dt"]).strftime("%m/%d")
            print(f"{time}={temp}")
            listx.append(time)
            listy.append(temp)

        icon_code = info['current']['weather'][0]['icon']
        weather_description = info['current']['weather'][0]['description']
        current_temperature = info['current']['temp']

        # 下載並保存天氣圖標
        icon_url = f"https://openweathermap.org/img/wn/{icon_code}@2x.png"
        response = requests.get(icon_url)
        with open(f"{icon_code}.png", "wb") as icon_file:
            icon_file.write(response.content)

        # 更新GUI
        image = Image.open(f"{icon_code}.png")  # 打開圖片
        tk_image = ImageTk.PhotoImage(image)  # 將圖片轉換為tkinter可以使用的格式
        icon_label.config(image=tk_image)  # type: ignore # 更新圖片
        icon_label.image = tk_image  # type: ignore # 避免被記憶體回收機制回收圖片

        temperature_label.config(text=f"溫度: {current_temperature}°C")
        description_label.config(text=f"描述: {weather_description}")

        font = FontProperties(fname='NotoSansTC-Black.otf', size=14)
        fig, ax = plt.subplots()
        ax.plot(listx, listy)
        ax.set_xlabel('日期', fontproperties=font)
        ax.set_ylabel('溫度', fontproperties=font)
        ax.set_title('天氣預測', fontproperties=font)
        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.draw()
        canvas = canvas.get_tk_widget()
        canvas.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

    else:  # 如果沒有main這個key，代表沒有天氣資訊
        description_label.config(text=f"描述: City Not Found")


def on_closing():
    window.destroy()
    plt.close('all')


def on_switch_change():
    global units, current_temperature
    if check_type.get():
        units = "metric"

    else:
        units = "imperial"

    if temperature_label.cget("text") != "溫度: ?°C":
        if units == "metric":
            current_temperature = round((current_temperature - 32) * 5 / 9, 2)
            temperature_label.config(text=f"溫度: {current_temperature}°C")
        elif units == "imperial":
            current_temperature = round(current_temperature * 9 / 5 + 32, 2)
            temperature_label.config(text=f"溫度: {current_temperature}°F")


font_size = 20
window = tk.Tk()
window.title("Weather App")
window.option_add("*font", ("Helvetica", font_size))
window.protocol("WM_DELETE_WINDOW", on_closing)

style = Style(theme="minty")
style.configure('my.TButton', font=('Helvetica', font_size))
style.configure('my.TCheckbutton', font=('Helvetica', font_size))

# 城市名稱輸入框
city_name_label = Label(window, text="目前的城市:?")
city_name_label.grid(row=0, rowspan=2, column=0)
lon_entry = Entry(window)
lon_entry.grid(row=0, column=1)
lat_entry = Entry(window)
lat_entry.grid(row=1, column=1)

# 查詢按鈕
search_button = Button(window,
                       text="獲得天氣資訊",
                       command=get_weather_info,
                       style='my.TButton')
search_button.grid(row=0, rowspan=2, column=2)

# 天氣圖標
icon_label = Label(window, text="天氣圖標")
icon_label.grid(row=2, column=0)

# 溫度標籤
temperature_label = Label(window, text="溫度: ?°C")
temperature_label.grid(row=2, column=1)

# 描述標籤
description_label = Label(window, text="描述: ?")
description_label.grid(row=2, column=2)

check_type = BooleanVar()
check_type.set(True)

check = Checkbutton(window,
                    variable=check_type,
                    onvalue=True,
                    offvalue=False,
                    command=on_switch_change,
                    text="溫度單位(°C/°F)",
                    style='my.TCheckbutton')
check.grid(row=3, column=1)

# 運行應用程式
window.mainloop()