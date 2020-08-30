# add
sum = 0
for i in range(1, 966+1):
    if i % 2 == 1:
        sum = sum + i
    else:
        sum = sum - i
print(sum)
