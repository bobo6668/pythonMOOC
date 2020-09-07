##f = open('latex.log', 'r')
##ls = []
##count = 0
##for line in f:
##    if line not in ls:
##        ls.append(line)
##        count += 1
####print(ls)
##print(count)

f = open('latex.log', 'r')
s = set()
count = 0
for line in f:
    if line not in s:
        s.add(line)
        count += 1
print('共{}关键行'.format(count))
