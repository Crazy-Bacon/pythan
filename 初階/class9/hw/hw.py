import random

ans = random.randint(1, 100)
mi = 0
ma = 100
while True:
    x = int(input(f"請輸入{mi}~{ma}的整數:"))
    if x == ans:
        print("恭喜猜中!")
        break
    elif x > ans:
        print("再小一點")
        if mi < x < ma:
            ma = x
    elif x < ans:
        print("再大一點")
        if mi < x < ma:
            mi = x
