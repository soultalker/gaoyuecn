import time as t
import random as r
start = t.perf_counter()
dirt = 1000*1000*1000
n = 0
for i in range(dirt+1):
    x,y = r.random(),r.random()
    if (pow(x**2+y**2,0.5)<1.0):
        n += 1
print('圆周率是：',4*n/dirt)
print('运行时间：{:.9f}s'.format(t.perf_counter()-start))
