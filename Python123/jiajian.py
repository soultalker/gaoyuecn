s = 1
k = 0
while (s < 967):
    if s%2 != 0:
        k = k + s
    else:
        k = k - s
    s += 1
print(k)
