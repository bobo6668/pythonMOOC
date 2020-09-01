#drawKoch.py 科赫雪花
import turtle as t
import os

def kochCurve(len, n):
    if n == 0:
        t.fd(len)
    else:
        for angle in [0, 60, -120, 60]:
            t.left(angle)
            kochCurve(len/3, n-1)

def main():
    # 初始化
    t.setup(600,600)
    t.penup()
    t.goto(-200, 100) # 直接goto移动
    t.pendown()
    t.pensize(2)
    # 画雪花
    level = 3 # 3阶科赫雪花，阶数
    for i in range(3):
        kochCurve(400, level)
        t.right(120)
    # 结束绘制
    t.hideturtle()
    t.done() # 避免绘画窗体 Python Turtle Graphics（未响应）而且可以保留绘画窗体不闪退


main()
