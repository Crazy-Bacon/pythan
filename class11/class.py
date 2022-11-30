bag = []
s = int(input("請輸入背包的大小"))
for i in range(s):
    t = input("請輸入想裝的東西")
    bag.append(t)
    print(bag)

bag2 = []
for i in bag:
    if not (i in bag2):
        bag2.append(i)
        print(f"{i}={bag.count(i)}")

# r = input("請輸入想那的東西")
# while r in bag:
#     bag.remove(r)

# print(bag)

# # c = input("請輸入想計算的東西:")
# # print(bag.count(c))
