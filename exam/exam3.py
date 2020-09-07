d = eval(input())
if type(d) == dict:
    d1 = {value:key for (key, value) in d.items()}
    print(d1)
else:
    print('输入错误')
