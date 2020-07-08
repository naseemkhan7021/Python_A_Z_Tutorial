print('''write = tringle,holow tringle,rectengle,holow rectengle
      dimand,holow dimand,holow rightangle,''')
paterns=['tringle','holow tringle','rectengle','holow rectengle','dimand',
        'holow dimand','holow rightangle']
y='yes'
while y=='yes':
    
    choice=input('enter the petern that you want = ')
    if choice in paterns:
        row=int(input('entar number of row = '))
        symbol=input('entar your symbol that you like = ')
        if choice=='tringle':
            for i in range(row+1):
                for j in range(1,(row+1)-i):
                    print(' ',end='')
                for k in range(1,i+1):
                    print(symbol,end='')
                for p in range(2,i+1):
                    print(symbol,end='')     
                print()

        elif choice=='holow tringle':
            for i in range(row+1):
                for j in range(1,(row+1)-i):
                    print(' ',end='')
                for k in range(1,i+1):
                    if k==1 or i==row:
                        print(symbol,end='')
                        continue
                    print(' ',end='')
                for p in range(2,i+1):
                    if p == i or i == row:
                         print(symbol,end='')
                         continue
                    print(' ',end='')      
                print()

        elif choice=='holow rectengle':
            column=int(input('entar number of column = '))
            for i in range(1,row+1):
                for j in range(1,column+1):
                    if i==1 or i==row or j==1 or j==column:
                        print(symbol,end='')
                        continue
                    print(' ',end='')
                print()

        elif choice=='rectengle':
            column=int(input('entar number of column = '))
            yn=input('you want sum spese yes/no = ')
                
            if yn=='yes':
                sp=int(input(' how many spase you want pleas wrinte = '))
                for i in range(1,row+1):
                    for j in range(1,sp+1):
                        print(' ',end='')
                    for k in range(1,column+1):
                        print(symbol,end='')
                    print()
            elif yn=='no':
                for i in range(1,row+1):
                    for k in range(1,column+1):
                        print(symbol,end='')
                    print()
            else:
                print('\nwrint only !!!! yes / no !!!!! ')
                    
        elif choice=='holow dimand':
            for z in range(1,row+1):
                for j in range(1,(row+1)-z):
                    print(' ',end='')
                for k in range(1,z+1):
                    if k==1:
                        print(symbol,end='')
                        continue
                    print(' ',end='')
                for p in range(2,z+1):
                    if p==z:
                        print(symbol,end='')
                        continue
                    print(' ',end='')
                print()


            for i in range(1,row+1):
                for j in range(1,i+1):
                    print(' ',end='')
                for q in range(1,(row+1)-i):
                    if q==1:
                        print(symbol,end='')
                        continue
                    print(' ',end='')
                for t in range((row-1)-i,0,-1):
                    if t==1:
                        print(symbol,end='')
                        continue
                    print(' ',end='')
                print()
        elif choice=='dimand':
            for z in range(1,row+1):
                for j in range(1,(row+1)-z):
                    print(' ',end='')
                for k in range(1,z+1):
                    print(symbol,end='')
                for p in range(2,z+1):
                    print(symbol,end='')
                print()


            for i in range(1,row+1):
                for j in range(1,i+1):
                        print(' ',end='')
                for q in range(1,(row+1)-i):
                    print(symbol,end='')
                for t in range((row-1)-i,0,-1):
                    print(symbol,end='')
                print()
        elif choice=='holow rightangle':
            side=input('rightangle shape right or left = ')
            if side=='right':
                for i in range(row+1):
                    for j in range(1,i+1):
                        if  i==row or j==1 or j==i:
                            print(symbol,end='')
                            continue
                        print(' ',end='')
                    print()
            elif side=='left':
                for i in range(row+1):
                    for k in range(1,(row+1)-i):
                        print(' ',end='')
                    for j in range(1,i+1):
                        if  i==row or j==1 or j==i:
                            print(symbol,end='')
                            continue
                        print(' ',end='')
                    print()
            else:
                print('pleas write only right / left!!!!')

    else:
        print('write only shape that mention in massege!!!!!!????????!!!!!!')
            
    D=input('do you want to cuntinue yes/no = ')
    y=D.lower()

else:
    print(' ok boss no problem !!!!!THANK!!!!!!! FOR USIN PROGRNAM')
