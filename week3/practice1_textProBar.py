#practice3.1 textProgressBar
import time as t

scale = 50
start = t.perf_counter()
for i in range(scale + 1):
    percent = i
    a = '*'* i
    b = '.'*(scale - i)
    dur = t.perf_counter() - start
    print("\r{0:3}% [{1}->{2}] {3:.3f}s".format(percent,a,b,dur), end = "")
    t.sleep(0.1)
    
