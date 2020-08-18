h = int(input('키를 입력하세요(cm):'))
w = int(input('몸무게를 입력하세요(kg):'))

BMI = w/h**2

if BMI>=25:
    print('비만입니다')
else :
    if BMI >= 23:
        print('과체중입니다')
    else :
        if BMI >=18.5:
            print('정상입니다')
        else :
            print('저체중입니다')
