# ['蘋果', '香蕉', '葡萄']

# []
# ['蘋果']
# ['a', 'b']
# [1, 2, 3]

# [1, 2] + ['b', 'c']

# [1, 2] * 2

# l = ['a', 'b', 'c']
# l[0]
# l[1]
# l[2]

# l = [0, 1, 2, 3, 4]
# l[0:3]
# l[3:5]

# len([])
# len(['蘋果'])
# len(['a', 'b'])
# len([1, 2, 3])

# l = ['a', 'b', 'c']
# for index in range(len(l)):
#     print(l[index])

# l = ['a', 'b', 'c']
# for element in l:
#     print(element)

# max([])
# max(['蘋果', '香蕉', '橘子'])
# max(['a', 'b'])
# max([1, 2, 3])

# min([])
# min(['蘋果', '香蕉', '橘子'])
# min(['a', 'b'])
# min([1, 2, 3])

# list('abc')
# list([4, 5, 6])
# list(range(3))
# '1,2,3'.split(',')
# '2020/1/1'.split('/')

# img = ['1', '2', '3']
# '-'.join(img)

# l = ['a', 'b', 'c']
# a = l.copy()
# a[0] = 1
# print(a, l)
juices = ['蘋果汁', '柳橙汁', '葡萄汁', '系統關閉']
while True:
    for index in range(len(juices)):
        print(f'{index+1}.{juices[index]}')
    # print("1. 蘋果汁")
    # print("2. 柳橙汁")
    # print("3. 葡萄汁")
    # print("4. 系統關閉")
    try:
        ans = int(input("請輸入編號:"))
    except:
        print("請輸入數字編號")
    else:
        if ans > len(juices) or ans <= 0:
            print("輸入錯誤查無此果汁，請重新輸入編號")
        elif ans == len(juices):
            print("~~系統關閉~~")
            break
        else:
            print(f"您點的商品是{juices[ans-1]}")

    #         print("您點的商品是蘋果汁")
    #     elif ans == 2:
    #         print("您點的商品是柳橙汁")
    #     elif ans == 3:
    #         print("您點的商品是葡萄汁")
    #     elif ans == 4:
    #         print("~~系統關閉~~")
    #         break
    #     else:
    #         print("輸入錯誤查無此果汁，請重新輸入編號")
    # git add .
# git commit -m "class9"
# git push