#AutoTraceDraw.py 参考代码
import turtle as t

#初始化
t.title('自动轨迹绘制')
t.setup(800, 600, 0, 0)
t.pencolor("red")
t.pensize(5)

#数据读取
datals = []
f = open("data.txt")
for line in f:
    line = line.replace("\n","")
    datals.append(list(map(eval, line.split(","))))
                  #先每个元素都执行eval，然后再把得到map转化成list
f.close()

#自动绘制
for i in range(len(datals)):
    t.pencolor(datals[i][3],datals[i][4],datals[i][5]) # 颜色
    t.fd(datals[i][0])      # 前进距离
    if datals[i][1]:        # 转向
        t.rt(datals[i][2])  # 角度
    else:
        t.lt(datals[i][2])