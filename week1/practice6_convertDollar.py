# Python练习1.5：货币转换
TempStr = input()
if TempStr[0:3]=="RMB": # 别漏了冒号:
    USDnum = eval(TempStr[3:])/6.78
    print("USD{:.2f}".format(USDnum)) # 记住格式化输出
elif TempStr[0:3]=='USD':
    RMBnum = eval(TempStr[3:])*6.78
    print("RMB{:.2f}".format(RMBnum))
