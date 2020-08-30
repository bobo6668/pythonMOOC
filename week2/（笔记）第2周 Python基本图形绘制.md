> [中国大学MOOC平台"Python语言程序设计" 第2周 Python基本图形绘制](https://www.icourse163.org/learn/BIT-268001?tid=1460270441#/learn/content?type=detail&id=1236349067)

## 2.1 深入理解Python语言

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7c1d1af3916545a78c7e7eeb34ccc98a~tplv-k3u1fbpfcp-zoom-1.image)

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c0faf192aa0c4d73b5f8a0592a53127c~tplv-k3u1fbpfcp-zoom-1.image)

## 2.2 实例2: Python蟒蛇绘制

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ffba2e9a24db47099b29448cfe63955e~tplv-k3u1fbpfcp-zoom-1.image)

```python
#PythonDraw.py
import turtle as t
t.setup(650, 350)   # 设置窗体大小，可以再加上窗体位置 200, 200
t.penup()
t.fd(-250)
t.pendown()
t.pensize(25)
t.pencolor("purple")
t.seth(-40)
for i in range(4):
    t.circle(40, 80)
    t.circle(-40, 80)
t.circle(40,80/2)
t.fd(40)
t.circle(16, 180)
t.fd(40 * 2/3)
t.done()
```

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e67e3a7dd15a4a50aa9381408978cb36~tplv-k3u1fbpfcp-zoom-1.image)

## 2.3 模块1: turtle库的使用

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7491afd0a02a4033bdf3ae5685fc23a6~tplv-k3u1fbpfcp-zoom-1.image)

## 2.4 turtle程序语法元素分析

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/05c9542c2d8242aab297b918112fe49d~tplv-k3u1fbpfcp-zoom-1.image)