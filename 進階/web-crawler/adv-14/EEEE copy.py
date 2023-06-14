from ttkbootstrap import *
from pppp.pppp import *
import time


def get_video_info_gui():
    _, _, _, _, res = get_video_info(lon_entry.get())
    res_option['menu'].delete(0, 'end')
    for r in res:
        res_option["menu"].add_command(label=r, command=tk._setit(res_var, r))
    res_var.set(res[0])


def dowload_video_gui():
    if download_video(lon_entry.get(), res_var.get(), show_progress):
        lat_entry.config(text="下載完成")
    else:
        lat_entry.config(text="解析度錯誤")


def start_progress():
    for i in range(101):
        progress['value'] = i
        percent_label.config(text=f"{i}%")
        window.update()
        time.sleep(0.05)


def show_progress(stream, chunk, bytes_remaining):
    percent = (100 * (stream.filesize - bytes_remaining)) / stream.filesize
    percent_label.config(text=f"{percent:.2f}%")
    progress['value'] = percent
    window.update()


window = tk.Tk()
city_name_label = Label(window, text="請輸入要下載的影片的網址")
city_name_label.grid(row=0, column=0)
lon_entry = Entry(window)
lon_entry.grid(row=0, column=1)
lat_entry = Label(window, text="請影片的解析度")
lat_entry.grid(row=1, column=0)
lat_entry = Label(window, text="")
lat_entry.grid(row=2, column=0)
search_button = Button(window, text="獲得影片資訊", command=get_video_info_gui)
search_button.grid(row=0, column=2)
download = Button(window, text="下載影片", command=dowload_video_gui)
window.title("Progress Bar Example")
download.grid(row=1, column=2)
progress = Progressbar(window,
                       orient=HORIZONTAL,
                       length=200,
                       mode='determinate')
progress.grid(row=2, column=1, padx=10, pady=10)
percent_label = Label(window, text="")
percent_label.grid(row=2, column=2, padx=10, pady=10)

res_var = tk.StringVar()
res_option = OptionMenu(window, res_var, ())
res_option.grid(row=1, column=1, padx=10, pady=10)
window.mainloop()