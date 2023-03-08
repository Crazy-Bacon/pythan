"""
請使用turtle模組、for、time模組來印出時鐘的秒針
基本功能參考影片t1_turtle_time.mp4
提示：
turtle.clear() # 清空畫面指令
​
import time  # 匯入time模組
time.sleep(1) # 延遲1秒
"""
import turtle as t
import time
for i in range(60):
    t.right(360 // 60 * i)
    t.forward(100)
    time.sleep(1)
    t.home()
    t.clear()
t.done()