# testTypes 测试一下输入 1,2,3，会是什么样的数据类型

a = input()
print(isinstance(a, str))   # √字符串
print(isinstance(a, list))
print(isinstance(a, tuple))

a = "{}".format(input())
print(isinstance(a, str))   # √字符串
print(isinstance(a, list))
print(isinstance(a, tuple))

a = eval("{}".format(input()))
print(isinstance(a, str))
print(isinstance(a, list))
print(isinstance(a, tuple)) # √元组

a = eval("1,2,3")
print(isinstance(a, str))
print(isinstance(a, list))
print(isinstance(a, tuple)) # √元组

# Results
"""
1,2,3
True
False
False
1,2,3
True
False
False
1,2,3
False
False
True
False
False
True
"""
