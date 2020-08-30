# calPi
import random as r
import time as t
TEST = 1000 * 1000
hits = 0
start = t.perf_counter()
for i in range(TEST + 1):
    x, y = r.random(), r.random()
    dist = ( x * x + y * y ) ** 0.5
    if dist <= 1:
        hits += 1
pi = 4 * ( hits / TEST )
print(pi)
print(t.perf_counter() - start)

