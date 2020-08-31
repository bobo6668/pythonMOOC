#drawSevenDigits
import turtle as t
# 画一条线
def drawLine(flag):
    t.pendown() if flag else t.pendown()
    t.fd(40)
    t.right(90)

# 画一个数字
def drawDigit(digit):
    # 数字有七段
    drawLine(True) if digit in [2, 3, 4, 5, 6, 8, 9] else drawLine(False) # 笔画1
    drawLine(True) if digit in [1, 3, 4, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if digit in [2, 3, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if digit in [2, 6, 8] else drawLine(False)
    t.left(90)
    drawLine(True) if digit in [4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if digit in [2, 3, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if digit in [1, 2, 3, 4, 7, 8, 9] else drawLine(False)

# 画多个数字

drawDigit('1')