# pwd = ''
# while pwd != '1234':
#     pwd = input('請輸入密碼:')
#     if pwd == '1234':
#         print('歡迎光臨')
#     else:
#         print('密碼錯誤, 請重新輸入!')

x = int(input('請輸入數字:'))
i = 2
while x % i != 0 and i != x:
    i += 1

if i == x:
    print("yes")
else:
    print("no")
