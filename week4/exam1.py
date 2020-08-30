#exam1
for i in range(1000, 10000):
    a = i // 1000
    b = (i % 1000) // 100
    c = (i % 100) // 10
    d = i % 10
    if pow(a, 4) + pow(b, 4) + pow(c, 4) + pow(d, 4) == i:
        print(i)
