# wordCloudthreeKingdoms.py

import wordcloud
import jieba

# 读取txt
threeKingdomsTxt = open("E:\\21_git\\pythonMOOC\\week6\\threekingdoms.txt", \
                            "rt", encoding = 'utf-8').read()
# 利用jieba库 分词 【√】
words = jieba.lcut(threeKingdomsTxt)
for word in words:
    if len(word) == 1:
        del word
# 转化为以空格分隔的字符串
txt = " ".join(words)

# 生成词云
wc = wordcloud.WordCloud(width = 1920, height = 1080, font_path="msyh.ttc", \
                            background_color = 'white') # 注意需要加载中文字体
wc.generate(txt)
wc.to_file('wordCloudthreeKingdoms.png')