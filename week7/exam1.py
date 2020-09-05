f = open('latex.log', 'r', encoding='utf-8')
count = 0
columnCount = 0
for line in f:
    line = line.strip("\n") ## 重要
    column = len(line)
    if column > 0 :
        count += 1
        columnCount += column
ave = round(columnCount/count)
print(ave)

# f = open("1.txt")
# s, c = 0, 0
# for line in f:
#     line = line.strip("\n")
#     if line == "":
#         continue
#     s += len(line)
#     c += 1
# print(round(s / c))