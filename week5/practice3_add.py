#practice3_add.py

def cmul(*s):
    m = 1
    for i in s:
        m *= i
    return m

print(eval("cmul({})".format(input())))

# 理解
"""
input()返回字符串

"cmul({})".format(input())是把字符串填到一个字符串里面，
得到eu仍然是字符串。如输入是1,2,3，会得到："cmul(1,2,3)"。
注意到此时相当于输入了(1,2,3)这个元组

eval("cmul({})".format(input()))是把字符串n的""去掉。
仍以上面的例子为例，"cmul(1,2,3)"去掉""，则得到cmul(1,2,3)，
相当于运行函数cmul(1,2,3)

最后print该函数的返回结果，即return的m
"""
