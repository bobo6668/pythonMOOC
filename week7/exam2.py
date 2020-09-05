f = open('data.csv', 'r', encoding = 'utf-8')
lines = f.readlines()
lines = lines[::-1] ## 重要【√】审题，需要所有行先倒序
for line in lines:
    line = line.strip("\n") ## 重要
    line = line.replace(' ','') ## 重要【√】去空格
    ls = line.split(',')
    ls = ls[::-1]
    print(';'.join(ls))

# with open('data.csv', 'r', encoding='utf-8') as f:
#     lines = f.readlines()
#     # 按行进行倒序排列
#     lines.reverse()  # 原地转换
#     # lines = lines[::-1]  # 利用切片进行倒序
    
#     for line in lines:
#         # 用分号(;)代替逗号(,)分割数据，无空格
#         line = line.strip('\n')
#         # line = line.replace('\n', '')
#         line = line.replace(' ', '')
#         # 每行数据倒序排列
#         t = line.split(',')
#         t.reverse()  # 原地倒序
#         # t = t[::-1]  # 切片倒序
#         # 输出转换后的数据
#         print(';'.join(t))