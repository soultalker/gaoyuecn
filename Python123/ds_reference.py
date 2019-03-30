print('Simple Assignment')
shoplist = ['apple','manago','carrot','banana']
mylist = shoplist # 两个变量均指向同一个对象
del shoplist[0]
print('showlist is',shoplist)
print('mylist is',mylist)
print('Copy by making a full slice')
mylist = shoplist[:] #切片将生成对象的一个副本
del mylist[0]
print('shoplist is',shoplist)
print('mylist is',mylist)