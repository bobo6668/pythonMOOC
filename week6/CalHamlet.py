#CalHamlet.py

def getText():
    # 读取txt 【√】
    txt = open("hamlet.txt", "rt").read()
    # 归一化处理 【√】
    txt = txt.lower()                               # 全部转化为小写
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':   # 替换掉所有特殊字符
        txt = txt.replace(ch, " ")
    return txt

HamletTxt = getText()           # 读取txt

words = HamletTxt.split()       # 默认以空格分隔，得到所有单词 【√】
counts = dict()                 # 利用字典统计词频 【√】
for word in words:              
    counts[word] = counts.get(word, 0) + 1

items = list(counts.items())    # 转化为list方便处理和排序 【√】
items.sort(key = lambda x:x[1], reverse = True) # 按照items的第二个元素排序，逆序 【√】

for i in range(10):             # 打印出词频统计前十位
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))