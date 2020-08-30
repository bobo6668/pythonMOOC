## （笔记）第1周 Python基本语法元素
### 1.1 程序设计基本方法
* 计算机与程序设计
* 编译与解释【√】
  * 静态语言：编译执行(C/C++, Java)
  * 脚本语言：解释执行(Python, JavaScript, PHP)
* 程序的基本编写方法【√】
  * 编程解决问题的基本步骤
    * 确定IPO (Input, Process, Output)
    * 编写程序
    * 调试程序
* 学习计算机编程的原因、误区

### 1.2 Python开发环境配置
* Python语言概述【√】
* Python基本开发环境IDLE【√】
* Python程序编写与运行【√】
  * 两种编程方式：交互式、文件式
  * 实例
    * 1：圆面积的计算
      ```python
      #CalCircle.py
      r = 25
      pi = 3.1415
      area = pi * r * r
      print(area)
      print("{:.2f}".format(area))
      ```
    * 2：同切圆的绘制
      ```python
      #TangentCircleDraw.py
      import turtle
      ## https://docs.python.org/zh-cn/3/library/turtle.html
      turtle.pensize(2)
      turtle.circle(10)
      turtle.circle(40)
      turtle.circle(80)
      turtle.circle(160)
      ```
      ![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a2400eec6aaf4a3c8301a1f32104d3fd~tplv-k3u1fbpfcp-zoom-1.image)
      
    * 3：五角星的绘制
      ```python
      #StarDraw.py
      from turtle import *
      color('black','red') # 第一个是画笔颜色，第二个是填充颜色
      begin_fill()
      for i in range(5):
          fd(200) # forward(distance)
          rt(144) # right(angle)
      end_fill()
      ```
      ![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f34ea09fdaca498898fa8625d4119047~tplv-k3u1fbpfcp-zoom-1.image)
  
      拓展：改为画一个正方形
      ```python
      from turtle import *
      color('black','red') # 第一个是画笔颜色，第二个是填充颜色
      begin_fill()
      for i in range(4):
          fd(200) # forward(distance)
          rt(90) # right(angle)
      end_fill()
      done()
      ```
     ![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fcf386307ef4425799f90cdab5b4da2b~tplv-k3u1fbpfcp-zoom-1.image)
  
* Python高级开发环境VSCode

### 1.3 实例1: 温度转换
* 温度转换问题分析【√】
  * 需求分析：两种温度体系之间的转换
  * 问题分析：
    * 计算部分的理解和确定
    * 分析问题
    * 划分边界
    * 输入输出格式设计
    * 设计算法
  * 实例编写（代码附在后面）
  * 举一反三【√】
    * 作为一个典例，理解Python的语法元素，快速入门Python语言
    * 改变输入输入的格式
    * 拓展到类似的问题：各类转换问题
### 1.4 Python语法元素分析
* 程序的格式框架
  * 代码高亮、缩进、注释
* 命名与保留字
* 数据类型
  * 字符串【√】
    * 序号：
      * 正向递增序号
      * 反向递减序号
    * 使用：获取字符串中一个或多个字符
      * 索引
      * 切片
  * 数字类型
    * 整数
    * 浮点数
  * 列表类型【√】
* 语句与函数
    * 赋值语句
    * 分支语句
    * 函数
* Python程序的输入输出
    * input()
    * print()
        * 基本使用格式
        * 格式化【√】
    * eval() 评估函数【√】
        * 去掉参数最外侧引号并执行余下语句的函数
* "温度转换"代码分析

## 代码复现
### “温度转换”
```python
#TempConvert.py
TempStr = input("请输入末尾为符号的温度值：")
if TempStr[-1] in ['F', 'f']:
    C = ( eval(TempStr[0:-1]) - 32 )/1.8 # 注意到从第1位到最后一位（不包括最后一位），是[0:1]
    print("转换后的温度是{:.2f}C".format(C)) # 记住格式化输出
elif TempStr[-1] in ['C','c']:
    F = 1.8 * eval(TempStr[0:-1]) + 32
    print("转换后的温度是{:.2f}F".format(F))
else:
    print("输入格式有误")
```
### 拓展：温度符号放在首位
```python
TempStr = input("请输入首位为符号的温度值：")
if TempStr[0] in ['F', 'f']:
    C = ( eval(TempStr[1:]) - 32 )/1.8 #注意到从第2位到字符串结束，是[1:]
    print("转换后的温度是C{:.2f}".format(C))
elif TempStr[0] in ['C','c']:
    F = 1.8 * eval(TempStr[1:]) + 32
    print("转换后的温度是F{:.2f}".format(F))
else:
    print("输入格式有误")
```
## 练习
### Python练习1.3：数字形式转换
```python
# Python练习1.3：数字形式转换
# 参考 https://blog.csdn.net/qq_33862675/article/details/89048935
InputNum = input()
DictHanzi = ['零','一','二','三','四','五','六','七','八','九']
Output = ''
for i in InputNum:
    Output = Output + DictHanzi[eval(i)]
print(Output)
```
### Python练习1.5：货币转换
```python
# Python练习1.5：货币转换
TempStr = input()
if TempStr[0:3]=="RMB": # 别漏了冒号:
    USDnum = eval(TempStr[3:])/6.78
    print("USD{:.2f}".format(USDnum)) # 记住格式化输出
elif TempStr[0:3]=='USD':
    RMBnum = eval(TempStr[3:])*6.78
    print("RMB{:.2f}".format(RMBnum))
```

---

2020年8月26日20:27:08 更新
## 小测试

> [Python如何垂直输出helloworld？ - 知乎](https://www.zhihu.com/question/268286498)

```python
for i in "hello world":
    print(i)
```

