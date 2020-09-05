#write and read csv

print('Reading...')
f1 = open('E:\\21_git\\pythonMOOC\\week7\\test.txt', 'r')

lsAll = []
for line in f1:
    line = line.replace('\n', '')   # 删掉行末换行符
    ls = line.split(',')            # 转换成为list
    # print(ls)
    lsAll.append(ls)                # 添加到总list，这是个二维列表
print(lsAll)
f1.close()
print('Reading... done!')


print('Writing...')
lsAll = [['国', '美', '本'], ['中国', '美国', '日本'], ['中', '美', '日']]
print(lsAll)

f2 = open('E:\\21_git\\pythonMOOC\\week7\\test.txt', 'w')

for item in lsAll:
    # print(item)
    s = ','.join(item) + '\n'
    # print(s)
    f2.write(s)
f2.close()
print('Writing... done!')