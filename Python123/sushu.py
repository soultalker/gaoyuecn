def sushu(c):
    a = 2
    while a < c:
        if (c%a!=0):
            a+=1
        else:
            break
    if a == c:
        return(c)
    else:
        return(0)
s = 3
for k in range(3,100):
    s = s+sushu(k)
print(s)