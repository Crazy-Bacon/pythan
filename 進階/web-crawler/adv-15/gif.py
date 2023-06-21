#######################匯入模組########################
from moviepy.editor import *  # pip install moviepy
import sys
import os
from pppp.pppp import *

#######################初始化########################
os.chdir(sys.path[0])  # 將工作目錄設置為目前檔案所在的目錄

#######################取得影片資訊########################
url = "https://www.youtube.com/watch?v=WlfIYn8-1pI"
title, author, length, thumbnail_url, res = get_video_info(url)
print(f"影片解析度:{res}")

#######################下載影片########################
r = input("根據上面的資訊, 請輸入要下載的影片的解析度(720p/480p/360p/240p/144p):")
result = "下載完成" if download_video(url, r) else "下載失敗"
print(result)

#######################切割影片########################
beg = int(input("請輸入要切割的開始時間(秒):"))
end = int(input("請輸入要切割的結束時間(秒):"))
result = "剪輯完成" if cut_video("【小小兵】第三支精采可愛預告.mp4", beg, end) else "剪輯失敗"
print(result)

#######################合併影片########################
file_name_list = [
    "【小小兵】第三支精采可愛預告-9-10.mp4", "【小小兵】第三支精采可愛預告-9-10.mp4",
    "【小小兵】第三支精采可愛預告-9-10.mp4"
]
result = "合併影片成功" if merge_video(file_name_list, "合併影片.mp4") else "合併影片失敗"
print(result)

#######################影片轉GIF########################
video_path = "合併影片.mp4"
gif_path = "合併影片.gif"
if os.path.isfile(video_path):
    clip = VideoFileClip(video_path)
    clip.write_gif(gif_path)
    print("影片轉GIF成功")
else:
    print("影片轉GIF失敗")