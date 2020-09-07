import jieba
txt = open('沉默的羔羊.txt', 'r', encoding ='utf-8').read()
words = jieba.lcut(txt)
# ls = []
counts = {}
for word in words:
    if len(word) >= 2:
        # ls.apppend(word)
        counts[word] = counts.get(word, 0) + 1

items = list(counts.items())    # 转化为list方便处理和排序
items.sort(key = lambda x:x[1], reverse = True) # 按照items的第二个元素排序，逆序
print(items[0][0])