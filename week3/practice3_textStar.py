# practice 3.3 textStar
inputNum = eval(input())
for i in range(inputNum + 1):
    if i % 2 == 0:
        continue
    a = '*' * i
    print(a.center(inputNum))

# reference
##n = eval(input())
##for i in range(1,n+1,2):
##    print("{0:^{1}}".format('*'*i, n))
