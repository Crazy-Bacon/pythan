from ttkbootstrap import *


def get_video():
    pass


def dowload():
    pass


window = tk.Tk()
city_name_label = Label(window, text="請輸入要下載的影片的網址")
city_name_label.grid(row=0, column=0)
lon_entry = Entry(window)
lon_entry.grid(row=0, column=1)
lat_entry = Label(window, text="請影片的解析度")
lat_entry.grid(row=1, column=0)
lat_entry = Label(window, text="")
lat_entry.grid(row=2, column=0)
search_button = Button(window, text="獲得影片資訊", command=get_video)
search_button.grid(row=0, column=2)
download = Button(window, text="下載影片", command=dowload)
download.grid(row=1, column=2)
window.mainloop()