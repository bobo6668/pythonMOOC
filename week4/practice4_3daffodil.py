# 3daffodil
s = ''
for i in range(100, 999 + 1):
    a = i // 100
    b = (i % 100) // 10
    c = i % 10
    if a ** 3 + b ** 3 + c ** 3 == i:
        s = s + str(i) + ',' # 先字符串加起来
print(s[0:-1]) # 然后字符串切片
