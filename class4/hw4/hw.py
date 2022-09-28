try:
    f = float(input("請輸入華氏溫度:"))
except:
    print('發生錯誤')
else:
    print('成功執行')
    c = 5 / 9 * (f - 32)
    print("華氏溫度" + str(f) + "等於華氏溫度" + str(c) + "C")
# git add .
# git commit -m "提示文字"
# git push