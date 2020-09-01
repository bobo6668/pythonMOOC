#solveHanoi
def Hanoi(n, src, dst, mid):
    global count # 需要声明是全局变量
    if n == 1: # 第1个盘子(最上面那个)
        print('{0}:{1}->{2}'.format(n, src, dst))
        count += 1
    else:
        # 把前n-1个从src搬运到mid
        Hanoi(n-1, src, mid, dst)
        # 把第n个(最后一个)从src搬运到dst
        print('{0}:{1}->{2}'.format(n, src, dst))
        count += 1
        # 再把前n-1个从mid搬运到dst
        Hanoi(n-1, mid, dst, src)

# 测试1：共2个盘子
count = 0
Hanoi(2, '源', '目标', '中间')
print('总次数 = {}'.format(count))

# 测试2：共3个盘子
count = 0
Hanoi(3, '源', '目标', '中间')
print('总次数 = {}'.format(count))