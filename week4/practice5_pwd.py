# pwd
flag = 0
for i in range(3):
    inputName = input()
    inputPwd = input()
    if inputName == 'Kate' and inputPwd == '666666':
        print('登录成功！')
        flag  = 1
        break
if flag == 0:
    print('3次用户名或者密码均有误！退出程序。')
