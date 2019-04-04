i = 0
while (i < 3):
    name = input()
    psw = input()
    if (name=='Kate')&(psw =='666666'):
        print('登录成功')
        break
    else:
        i += 1
print('3次用户名或者密码均有误')