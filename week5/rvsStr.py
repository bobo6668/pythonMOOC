#reverseStr.py 字符串反转
def rvsStr(s):
    if s == "" :
        return s # 别漏了s...
    else :
        return rvsStr(s[1:]) + s[0] # 分成两部分：第一个字符+其余字符，建立递归链条

print(rvsStr('hello world'))

# 当然，可以直接用 s[::-1]