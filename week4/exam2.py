#exam2
sum = 0
for i in range(2,100 + 1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        sum = sum + i
print(sum)
        
