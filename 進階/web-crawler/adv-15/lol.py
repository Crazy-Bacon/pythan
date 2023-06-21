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
file_name1 = input("請輸入影片名稱:")
file_name2 = file_name1
file_name3 = file_name1
# 設定要合併的影片檔案
video1 = VideoFileClip(file_name1)
video2 = VideoFileClip(file_name2)
video3 = VideoFileClip(file_name3)

# 將影片檔案合併
final_clip = concatenate_videoclips([video1, video2, video3])

# 儲存影片檔案
final_clip.write_videofile("合併影片.mp4")
