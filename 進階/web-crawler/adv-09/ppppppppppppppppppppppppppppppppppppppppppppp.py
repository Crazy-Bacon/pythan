import matplotlib.pyplot as plt
import requests
import os
import sys
import datetime
from matplotlib.font_manager import FontProperties
from ttkbootstrap import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

os.chdir(sys.path[0])


def on_closing():
    window.destroy()
    plt.close('all')


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

    font = FontProperties(fname='NotoSansTC-Black.otf', size=14)
    fig, ax = plt.subplots()
    ax.plot(listx, listy)
    ax.set_xlabel('日期', fontproperties=font)
    ax.set_ylabel('溫度', fontproperties=font)
    ax.set_title('天氣預測', fontproperties=font)
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas = canvas.get_tk_widget()
    canvas.grid(row=0, column=0, padx=10, pady=10)


window = tk.Tk()
window.protocol("WM_DELETE_WINDOW", on_closing)
style = Style(theme="minty")

draw_button = Button(window, text="Draw Graph", command=draw_graph)
draw_button.grid(row=1, column=0, padx=10, pady=10)

window.mainloop()