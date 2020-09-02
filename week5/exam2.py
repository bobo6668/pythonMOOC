# exam2 连续质数计算

def prime(m):
    global count, s  # 声明是全局变量
    if count == 5:
        return 
    else:
        for i in range(2, m//2):
            if m % i == 0:
                break
        else:
            s = s + str(m) + ','  # 注意
            count += 1
##            print(m)
        prime(m + 1)

a = eval(input())
n = int(a)
n = n + 1 if n < a else n # 输出一个比a大的整数。
                          # 注意 else n 是 n = n 的意思

count = 0
s = ''
prime(n) # 调用程序
print(s[0:-1])
