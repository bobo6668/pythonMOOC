#CalThreeKingdoms.py
import jieba
           
# 读取txt 【√】                                       # 要补充编码【√】
threeKingdomsTxt = open("threekingdoms.txt", "rt", encoding="utf-8").read()

# 利用jieba库 分词 【√】
words = jieba.lcut(threeKingdomsTxt)   

# 利用字典统计词频
counts = dict()                 
for word in words:
    if len(word) == 1:  # 剔除单字，显然不是人名（也顺带剔除了标点符号）【√】
        continue
    elif word == '玄德' or word == '玄德曰': # 处理别名【√】
        rword = '刘备'
    elif word == '关公' or word == '云长':
        rword = '关羽'
    elif word == '孔明曰' or word == '诸葛亮':
        rword = '孔明'
    elif word == '丞相' or word == "孟德":
        rword = '曹操'
    else:
        rword = word
    counts[rword] = counts.get(rword, 0) + 1

# 剔除非人名 【√】
for i in ['却说', '将军', '二人', '不可', '荆州', '不能', '如此', '主公', \
            '军士', '商议', '如何', '引兵', '次日', '左右', '军马', '大喜', \
            '天下', '东吴', '于是', '今日', '不敢', '魏兵', '陛下', '一人', \
            '都督', '人马', '不知', '汉中', '只见']:
    del counts[i]

items = list(counts.items())    # 转化为list方便处理和排序
items.sort(key = lambda x:x[1], reverse = True) # 按照items的第二个元素排序，逆序

for i in range(10):             # 打印出词频统计前10位
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))
