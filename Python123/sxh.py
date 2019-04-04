n = 100
k = 0
while n <= 999:
    a = int(n/100)
    b = int((n-a*100)/10)
    c = n-a*100-b*10
    if n == a**3+b**3+c**3:
        print(n,end=',')
    n += 1