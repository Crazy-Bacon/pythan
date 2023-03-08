"""
請使用turtle模組以及for印出以下圖形
t0_turtle_stamp.jpg
提示：
turtle.home()是讓烏龜回到原點的指令
"""
import turtle as t

t.shape("turtle")
t.penup()
t.stamp()
for i in range(9):
    t.forward(100)
    t.stamp()
    t.home()
    t.right(360 // 8 * i)
t.done()
