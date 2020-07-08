### this is my owen program to find age in year week and days

from datetime import date
ye='yes'
while ye=='yes':
    n1=input('entar your name ')
    # birth date info muliple user input
    b_y,b_m,b_d=input('''please entar your birth date like this 
                        ---> (yyyy/mm/dd) = ''').split('/')
    # changing str ---> int
    y1=int(b_y)
    m1=int(b_m)
    d1=int(b_d)
    # this is for ---> (yyyy/mm/dd)
    dob     =  date(y1,m1,d1)

    # this is condition for chocing currant date or user input date
    print('1 = for current date \n 2 = for enter ending date that you like')
    c_n=int(input('please choice number 1 or 2 ='))

    # condition for chusing currant date
    y_1=dob.year
    if c_n==1:
        today=date.today()
        y_2=today.year
        while y_1<=y_2:
            if y_1%4==0 or y_1%100!=0 and y_1%400==0:
                print('leep year is ',y_1)
            y_1+=1
        # total days finding
        td1=(today-dob).days
        # year week and days that user age
        y=int(td1/365)
        w=int((td1%365)/7)
        d=(td1%365)%7
        print(f'total days {n1} leave on erth = {td1}')
        print('year = ',y,' week = ',w,' days = ',d)

    else:
        # eding date that user input
        u_y,u_m,u_d=input('''please entar your date that you like this 
                        ---> (yyyy/mm/dd) = ''').split('/')
        # changing str ---> int
        y2=int(u_y)
        m2=int(u_m)
        d2=int(u_d)
        last_d  =  date(y2,m2,d2)
        y_3=last_d.year
        while y_1<=y_3:
            if y_1%4==0 or y_1%100!=0 and y_1%400==0:
                print('leep year is ',y_1)
            y_1+=1
        # total days finding
        td2=(last_d-dob).days
        # year week and days that user age
        y=int(td2/365)
        w=int((td2%365)/7)
        d=(td2%365)%7

        print(f'total days --{n1}-- leave on erth = {td2}')
        
        print('year = ',y,' week = ',w,' days = ',d)
    r=input('Do you want to continue yes/no = ' )
    ye=r.lower()
else:
    print(' no problem boss!!!!!! THANK FOR USING PROGRAM !!!!!')
