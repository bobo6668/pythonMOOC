# 我的解答，有误
# try:
#     inputStr = input()
#     inputNum = eval(inputStr)
#     if type(inputNum) == float or type(inputNum) == int or type(inputNum) == complex:
#         print(inputNum ** 2)
# except:
#     print('输入有误')

## 参考答案
## complex()和complex(eval())之间的比较将能够排除非数字类型的输入。
## 注意：不能直接使用eval()，否则，用户可以通过输入表达式（如100**2）输入数字，与要求不同（在实际应用中带来安全隐患）。

s = input()
try:
    if complex(s) == complex(eval(s)):
        print(eval(s)**2)
except:
    print("输入有误")