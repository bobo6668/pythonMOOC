#drawSevenDigits
import turtle as t
import time as time

# 绘制数码管间隔：每一段都留一定空白，更美观
def drawGap():
    t.penup()
    t.fd(5)

# 绘制单段数码管：画一条线
def drawLine(flag):
    drawGap()
    t.pendown() if flag else t.penup()
    t.fd(40)
    drawGap()
    t.right(90)

# 根据数字绘制七段数码管：画一个数字
def drawDigit(digit):
    # 数码管有七段，按固定顺序绘制
    drawLine(True) if digit in [2, 3, 4, 5, 6, 8, 9] else drawLine(False) # 笔画1
    drawLine(True) if digit in [0, 1, 3, 4, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 2, 3, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 2, 6, 8] else drawLine(False)
    t.left(90)
    drawLine(True) if digit in [0, 4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 2, 3, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 1, 2, 3, 4, 7, 8, 9] else drawLine(False)
    t.left(180) # 转回去(水平向右)，为绘制其他数字做好准备
    t.penup()
    t.fd(20)    # 为绘制其他数字确定起点位置

# 画多个数字
def drawData(data):
    # 设输入的数据类型是“2020+09-01=”，希望绘制成“2020年09月01日”
    t.pencolor('red')
    for i in data:
        if i == '+':
            t.write('年', font = ('Arial', 18, 'normal')) # 绘制汉字
            t.fd(40)
            t.pencolor('green')
        elif i == '-':
            t.write('月', font = ('Arial', 18, 'normal'))
            t.fd(40)
            t.pencolor('blue')
        elif i == '=':
            t.write('日', font = ('Arial', 18, 'normal'))
            t.fd(40)
        else:
            drawDigit(eval(i))

def main():
    # 初始化
    t.setup(800, 350, 200, 200)
    t.penup()
    t.fd(-300)
    t.pensize(5)
    # 绘制当前日期
    drawData(time.strftime('%Y+%m-%d=', time.gmtime()))
    # 结束绘制
    t.hideturtle()
    t.done() # 避免绘画窗体 Python Turtle Graphics（未响应）而且可以保留绘画窗体不闪退
    
main()
