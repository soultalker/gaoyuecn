import random as r
k = eval(input())
c = 0
r.seed(123)
for i in range(k+1):
    x,y = r.random(),r.random()
    if pow((x**2+y**2),0.5) <= 1:
        c += 1
pi = 4*c/k
print('{:.6f}'.format(pi))