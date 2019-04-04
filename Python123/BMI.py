#BMI.py
height,weight = eval(input('请输入身高（米）和体重（千克），用逗号分隔'))
bmi = weight/(height**2)
print('您的BMI为{:.2f}'.format(bmi))
#int,nat = '',''
if bmi < 18.5:
    int,nat = 'thin','thin'
elif 18.5 <= bmi < 24:
    int,nat = 'normal','normal'
elif 24 <= bmi < 25:
    int,nat = 'nomal','str'
elif 25<= bmi < 28:
    int,nat = 'str','str'
elif 28 <= bmi <30:
    int,nat = 'sta','fat'
else:
    int,nat = 'fat','fat'
print('BMI is 国际{},国内{}.'.format(int,nat))
