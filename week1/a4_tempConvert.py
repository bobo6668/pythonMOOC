#TempConvert.py
TempStr = input("请输入末尾为符号的温度值：")
if TempStr[-1] in ['F', 'f']:
    C = ( eval(TempStr[0:-1]) - 32 )/1.8 # 注意到从第1位到最后一位（不包括最后一位），是[0:1]
    print("转换后的温度是{:.2f}C".format(C))
elif TempStr[-1] in ['C','c']:
    F = 1.8 * eval(TempStr[0:-1]) + 32
    print("转换后的温度是{:.2f}F".format(F))
else:
    print("输入格式有误")

###拓展
##TempStr = input("请输入首位为符号的温度值：")
##if TempStr[0] in ['F', 'f']:
##    C = ( eval(TempStr[1:]) - 32 )/1.8 #注意到从第2位到字符串结束，是[1:]
##    print("转换后的温度是C{:.2f}".format(C))
##elif TempStr[0] in ['C','c']:
##    F = 1.8 * eval(TempStr[1:]) + 32
##    print("转换后的温度是F{:.2f}".format(F))
##else:
##    print("输入格式有误")
