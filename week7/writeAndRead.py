fname = "E:\\21_git\\pythonMOOC\\week7\\test.txt"

writels = ['中国', '美国', '日本']
f1 = open(fname, 'w')
f1.write(' '.join(writels))
print('Writing test.txt... done')
f1.close()

f2 = open(fname, 'r')
print('Reading test.txt...')
readls = f2.readline().split()
print(readls)
f2.close()
