# wordCloudthreeKingdoms.py

import wordcloud
import jieba
from imageio import imread #【√】
mask = imread("star2.png")  #【√】

# 读取txt
threeKingdomsTxt = open("新时代中国特色社会主义.txt", \
                            "rt", encoding = 'utf-8').read()
# 利用jieba库 分词 【√】
words = jieba.lcut(threeKingdomsTxt)
# for word in words:
#     if len(word) == 1:
#         del word
# 转化为以空格分隔的字符串
txt = " ".join(words)

# 生成词云                # 注意图片大小实际取决于mask   # 注意需要加载中文字体
wc = wordcloud.WordCloud(width = 1920, height = 1080, font_path="msyh.ttc", \
                            background_color = 'white', mask = mask) #【√】
wc.generate(txt)
wc.to_file('wordCloud新时代中国特色社会主义.png')