# num = int(input("請輸入想要存幾筆資料"))
# b = {}
# for i in range(num):
#     key = input("請輸入標籤名稱:")
#     value = input("請輸入資料")
#     b[key] = value
#     print(b)

# r = input("輸入想要刪的資料")
# b.pop(r, "")
# print(b)

# for key, value in b.items():
#     print(key + ":" + value)

# f = input("請輸入想搜尋的資料")
# print(f in b)
a = {}
while True:

    for key, value in a.items():
        print(key + ":" , value)
    print("1.新增科目")
    print("2.移除某科目")
    print("3系統關閉")
    e = input("請輸入功能選項:")
    if e == "1":
        key = input("請輸入科目名稱:")
        value = int(input("請輸入該科分數:"))
        a[key] = value
    elif e == "2":
        key2 = input("請輸入想要刪的科目名稱:")
        a.pop(key2, "")
    elif e == "3":
        print(f"平均是{sum(a.values())/len(a)}")
        break