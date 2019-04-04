n = 9999
while n > 999:
    a = int(n / 1000)
    b = int(n - a * 1000) / 100
    c = int(n - a * 1000 - b * 100) / 10
    d = n - a * 1000 - b * 100 - c * 10
#    if (n == (a ** 4 + b ** 4 + c ** 4 + d ** 4)):
    print(n,a,b,c,d)
    n -= 1
