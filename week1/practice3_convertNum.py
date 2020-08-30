# Python练习1.3：数字形式转换
# 参考 https://blog.csdn.net/qq_33862675/article/details/89048935

InputNum = input()
DictHanzi = ['零','一','二','三','四','五','六','七','八','九']
Output = ''
for i in InputNum:
    Output = Output + DictHanzi[eval(i)]
print(Output)
