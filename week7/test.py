# 读 测试
f = open("E:\\21_git\\pythonMOOC\\week7\\test.txt", 'rt', encoding = "utf-8")
print(f.read())
f.close()

f = open("E:\\21_git\\pythonMOOC\\week7\\test.txt", 'rt', encoding = "utf-8")
print(f.readline())
f.close()

f = open("E:\\21_git\\pythonMOOC\\week7\\test.txt", 'rt', encoding = "utf-8")
print(f.readlines()) # 是列表
f.close()

# 读 测试
f = open("E:\\21_git\\pythonMOOC\\week7\\test.txt", 'wt', encoding = "utf-8")
f.writelines(["中华人民共和国", "\n", "hello"])
f.close