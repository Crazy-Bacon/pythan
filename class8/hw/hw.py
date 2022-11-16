"""
輸入一數字n為尋找的區間範圍, 找出區間範圍
3,7的倍數顯示在螢幕上, 其餘不顯示
​
hint:可以使用%取餘數進行判斷
​
EX
請輸入正整數:20
3
6
7
9
12
14
15
18
"""
a = int(input("請輸入開始整數"))
b = int(input("請輸入結束整數"))

for x in range(a, b):
    i = 2
    while x % i != 0 and i != x:
        i += 1

    if i == x:
        print(x)
#git add .
# git commit -m "class8"
# git push