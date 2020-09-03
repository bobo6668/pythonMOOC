#exam1.py
inputStr = input()
t = set(inputStr)
##print(t)
sum = 0
for i in t:
    sum = sum + eval(i)
print(sum)
