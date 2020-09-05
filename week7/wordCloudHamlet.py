# wordCloudHalmet.py

import wordcloud

# 读取txt
txt = open("E:\\21_git\\pythonMOOC\\week6\\hamlet.txt", "rt").read()
# 归一化处理【√】
txt = txt.lower()                               # 全部转化为小写
for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':   # 替换掉所有特殊字符
    txt = txt.replace(ch, " ")
# 至此，已转化为以空格分隔的字符串

# 生成词云
wc = wordcloud.WordCloud(width = 1920, height = 1080)
wc.generate(txt)
wc.to_file('wordCloudHamlet.png')