# import turtle as t
# t.pensize(5)
# t.pencolor("yellow")
# t.fillcolor("yellow")
# t.tracer(0, 0)
# t.begin_fill()
# for i in range(5):
#     t.forward(300)
#     t.right(144)
# t.end_fill()
# t.done()import turtle as t

n = int(input("請輸入整數"))
s = 0
for i in range(1, n + 1):
    s = s + i
    print(s)
