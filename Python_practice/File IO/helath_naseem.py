# halath managment program

client_list={1:'naseem',2:'salman',3:'alim'}
log_list={1:'food',2:'exersice'}


def getdate():
    from datetime import date
    return date.today()

while True:
    try:
        # for globle use client
        for key,value in client_list.items():
            print('press',key,' to log ',value,'\n',end='')
        client_name=int(input('select number = '))
        o=client_list[client_name]

        print('log for 1')
        print('retrieve for 2')
        op=int(input('select number = '))
        if op is 1:
            # for key,value in client_list.items():
            #     print('press ',key,' for ',value,'\n',end='')
            # client_name=int(input('select number = '))
            for key,value in log_list.items():
                print('press',key,' to log ',value,'\n',end='')
            log_name=int(input('select number = '))
            # o=client_list[client_name]
            p=log_list[log_name]
            print('selected client : ',o)
            print('selected job : ',p)
            with open(o+'.txt','a') as f:
                k='y'
                while k=='y':
                    mytext=input(f'enter {p} = ')
                    f.write('['+str(getdate())+'] :'+ mytext+'\n')
                    l=input('Add more y/n: ')
                    k=l.lower()

                    # continue
                else:
                    print('No problame Thank of using program')
                break
                
        elif op is 2:
            
            print()
            with open(o+'.txt') as f:
                print(f.read())
                break
        else:
            print('Please enter for given option !!')
    except Exception:
        print('please enter valide number  !!!')