from tkinter import *
from tkinter import ttk,messagebox 
from datetime import date
import random
import pymysql
import pandas as pd
from csv import DictWriter




def append_dict_as_row(file_name, dict_of_elem, field_names):       #to creat the .csv file
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        dict_writer = DictWriter(write_obj, fieldnames=field_names)
        # Add dictionary as wor in the csv
        dict_writer.writerow(dict_of_elem)
dic={}
def submit1():
    try:
        #connect to the database

        connection = pymysql.connect(host='localhost',user='root',password='',database='bank_database')

        #connect() inbuilt function of pymysql library
        #connection user defined object

        print('connection successful!!')
    except Exception:
        messagebox.showinfo("Error","Data server Error !!! \n (Please check Database servar)")

    #cursor user defined object
    cursor = connection.cursor() # cursor inbuilt method of pymysql.connect() ,to active(open) the connection
    #q user defined
    q= """INSERT INTO customers (CustName,CustID,AcOpeningDate,JointHolderName,Address,City,PinCode,State,Country,
                                    ResTelNo,MobilNo,Occupation,AcType,AcNo)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

    try:
        if len(M.get())==10 and len(T.get())==10:
            #Esecute cursor and pass query of student and data of student
            #user defind input
            cname=n.get()
            cid=random.randint(100000,999999)
            acod=d.get()
            Jhln=no.get()
            Ad=A.get()
            ci=C.get()
            PC=Pc.get()
            St=s.get()
            Cn=Co.get()
            RTno=T.get()
            Mno=M.get()
            Oction=Occupt.get()
            AcTp=AcT.get()
            Acno=random.randint(100000000000000,999999999999999)
            

            val=(cname,cid,acod,Jhln,Ad,ci,PC,St,Cn,RTno,Mno,Oction,AcTp,Acno)
            cursor.execute(q,val) #run sql query and data send from puthon to mysql here execute() inbuilt method of cursor
            connection.commit() #to save action in table through query

            field_names=['CustName','CustID','AcOpeningDate','JointHolderName','Address','City','PinCode','State','Country','ResTelNo','MobilNo'
                        ,'Occupation','AcType','AcNo'
                        ]

            # dict for store the data
            dic={'CustName':cname,'CustID':cid,'AcOpeningDate':acod,'JointHolderName':Jhln,'Address':Ad,'City':ci,
                    'PinCode':PC,'State':St,'Country':Cn,'ResTelNo':RTno,'MobilNo':Mno,'Occupation':Oction,'AcType':AcTp,'AcNo':Acno}
             
            
            append_dict_as_row('cutomer_info.csv',dic,field_names)      #to creat the .csv file

            print(cursor.rowcount, "Record Inserted")
            print('Your details is here \n Check your details and note it ')
            print(dic)  # print only one row data

            messagebox.showinfo("Alert","The Record is successfully inserted !!! \n (ThanYou for opening account)")
            cutname_E.delete(0, END)
            Acdate_E.delete(0, END)
            Nomini_E.delete(0, END)
            Adderess_E.delete(0, END)
            City_E.delete(0, END)
            Pincod_E.delete(0, END)
            State_E.delete(0, END)
            Country_E.delete(0, END)
            TelNo_E.delete(0, END)
            mobile_E.delete(0, END)

        else:
            messagebox.showinfo("Error","Mobile or Telphone No. is error !!! \n (Please Enter 10 digits No.)")
            mobile_E.delete(0, END)
            TelNo_E.delete(0, END)
    except Exception:
        print("sumthing is wrong")

def showcutom_dedails(file_name):   # using pandas to read .csv file

    cutomfile=pd.read_csv('cutomer_info.csv')
    print(cutomfile)

def searchrecord():
    #connect to the database

    connection = pymysql.connect(host='localhost',user='root',password='',database='bank_database')
    #connect() inbuilt function of pymysql library
    #connection user defined object
    print('connection successful!!')

    cursor = connection.cursor()      # to active(open) the connection


    q="select * from customers where AcNo=%s"
    cutmAC=cutAccountno_E.get()
    # Execute cursor
    cursor.execute(q,cutmAC)  #run SQL query aconn.commit() to save action in table through query 
    records=cursor.fetchall() # records user defined object which hold no. of rows and columns means hod table
    print('Total number of rows in customers is : ', cursor.rowcount)
    for row in records:
        print("Cutomer name         : ",row[0])
        print("Cutomer Id           :",row[1])
        print("Accoutn opening date : ",row[2])
        print("Joint holder name    : ",row[3])
        print("Address              : ",row[4])
        print("City                 : ",row[5])
        print("Pincode              : ",row[6])
        print("State                : ",row[7])
        print("Country              : ",row[8])
        print("Teliphone no.        : ",row[9])
        print("Mobile no.           : ",row[10])
        print("Occupation           : ",row[11])
        print("Actype               : ",row[12])
        print("Ac No.               : ",row[13])
        break
    else:
        messagebox.showinfo("Error","Account no. does not exist !!! \n (Please Account no. and retry)")


def customTransection():
    data=pd.read_csv('cutomer_info.csv')
    TF=str(data.loc[data['AcNo']==int(cutAccountno_E.get())])
    if TF=='':
        messagebox.showinfo("Error","Account no. does not exist !!! \n (Please Account no. and retry)")

    else:
        
        #connect to the database

        connection = pymysql.connect(host='localhost',user='root',password='',database='bank_database')

        #connect() inbuilt function of pymysql library
        #connection user defined object

        print('connection successful!!')

        # #cursor user defined object
        cursor = connection.cursor() # cursor inbuilt method of pymysql.connect() ,to active(open) the connection
        # q user defined
        
        q= """INSERT INTO cutomerstransaction (CustomerAcNo,Date,Particulars,AmtWithdrown,AmtDeposited,Balance)
                                    VALUES (%s,%s,%s,%s,%s,%s)"""


d = {1:"new Account",2:'Account info',3:'withdro money',4:'Deposit monye'}
print("pleas type number for folowing comment")

for k,v in d.items():
    print(f"{k} for {v}")
op=int(input("enter your option -->"))




if op==1:
    wd=Tk()
    wd.title('New Account')

    # flat, groove, raised, ridge, solid, or sunken   <-- this is border style

    HTitle=Label(wd,text='Enter Customer Dedails',fg="#06a099",font=("Arial",20))
    HTitle.config(font=("Sylfaen", 30))
    HTitle.grid(row=0,column=1,columnspan=4)
    
    # labels 
    cutname_L=Label(wd,text="Customer name :",font=("Arial"),padx=10,pady=10)
    cutname_L.grid(row=1,column=0)
    Acodate_L=Label(wd,text="Account oppening date :",font=("Arial"),padx=10,pady=10)
    Acodate_L.grid(row=1,column=2)
    Nomini_L=Label(wd,text="Joint holder name :",font=("Arial"),padx=10,pady=10)
    Nomini_L.grid(row=2,column=0)
    Adderess_L=Label(wd,text="Adderess :",font=("Arial"),padx=10,pady=10)
    Adderess_L.grid(row=2,column=2)
    City_L=Label(wd,text="city name :",font=("Arial"),padx=10,pady=10)
    City_L.grid(row=3,column=0)
    PinCod_L=Label(wd,text="Pin code :",font=("Arial"),padx=10,pady=10)
    PinCod_L.grid(row=3,column=2)
    State_L=Label(wd,text="State name :",font=("Arial"),padx=10,pady=10)
    State_L.grid(row=4,column=0)
    Country_L=Label(wd,text="Country name :",font=("Arial"),padx=10,pady=10)
    Country_L.grid(row=4,column=2)
    TelNo_L=Label(wd,text="Telphone No. :",font=("Arial"),padx=10,pady=10)
    TelNo_L.grid(row=5,column=0)
    MobileNo_L=Label(wd,text="Mobile No.` :",font=("Arial"),padx=10,pady=10)
    MobileNo_L.grid(row=5,column=2)


    # Entry
    n=StringVar()
    d=StringVar()
    no=StringVar()
    A=StringVar()
    C=StringVar()
    Pc=StringVar()
    s=StringVar()
    Co=StringVar()
    T=StringVar()
    M=StringVar()
    cutname_E=Entry(wd,textvariable=n)
    cutname_E.grid(row=1,column=1,padx=10,pady=10)
    Acdate_E=Entry(wd,textvariable=d)
    Acdate_E.grid(row=1,column=3,padx=10,pady=10)
    Nomini_E=Entry(wd,textvariable=no)
    Nomini_E.grid(row=2,column=1,padx=10,pady=10)
    Adderess_E=Entry(wd,textvariable=A)
    Adderess_E.grid(row=2,column=3,padx=10,pady=10)
    City_E=Entry(wd,textvariable=C)
    City_E.grid(row=3,column=1,padx=10,pady=10)
    Pincod_E=Entry(wd,textvariable=Pc)
    Pincod_E.grid(row=3,column=3,padx=10,pady=10)
    State_E=Entry(wd,textvariable=s)
    State_E.grid(row=4,column=1,padx=10,pady=10)
    Country_E=Entry(wd,textvariable=Co)
    Country_E.grid(row=4,column=3,padx=10,pady=10)
    TelNo_E=Entry(wd,textvariable=T)
    TelNo_E.grid(row=5,column=1,padx=10,pady=10)
    mobile_E=Entry(wd,textvariable=M)
    mobile_E.grid(row=5,column=3,padx=10,pady=10)

    # combobuttons  accoute type

    Acctype=Label(wd,text="Account type :",font=("Arial"),padx=10,pady=10)
    Acctype.grid(row=6,column=0)
    # AcT=StringVar

    # combobox 1
    AcT=ttk.Combobox(wd)      # month user define object of combox(dropedowne menu)

    AcT["values"]=('Saving','Currant','Fixed')
    AcT.grid(row=6,column=1)
    AcT.current(1)



    # combobox 2
    Occupt_L=Label(wd,text="Choice your occupation :",font=("Arial"),padx=10,pady=10)
    Occupt_L.grid(row=6,column=2,padx=10,pady=10)

    Occupt=ttk.Combobox(wd)      # month user define object of combox(dropedowne menu)

    Occupt["values"]=('Student','Doctor','Businessman','House wifi','other')
    Occupt.grid(row=6,column=3)
    Occupt.current(1)

    #Button
    subBottun1=Button(wd,text="Submit",command=submit1,borderwidth=4,font="Times 12 bold",relief=RAISED,height=1,width=12)
    subBottun1.grid(row=8,column=1,columnspan=4)




    wd.mainloop()

elif op==2:
    wd1=Tk()

    wd1.title('Account Info')

    HTitle2=Label(wd1,text='Account info',fg="#06a099",font=("Arial",20))
    HTitle2.config(font=("Sylfaen", 30))
    HTitle2.grid(row=0,column=1,columnspan=4)

    # lable 
    cutname_L=Label(wd1,text="Customer name :",font=("Arial"),padx=10,pady=10)
    cutname_L.grid(row=1,column=0)
    cutAccountno_L=Label(wd1,text="Customer Account no. : ",font=("Arial"),padx=10,pady=10)
    cutAccountno_L.grid(row=1,column=3)

    # Entry
    nm=StringVar
    cutname_E=Entry(wd1,textvariable=nm,font=("Arial"))
    cutname_E.grid(row=1,column=2,padx=10,pady=10)
    cutAccountno_E=Entry(wd1,font=("Arial"))
    cutAccountno_E.grid(row=1,column=4,padx=10,pady=10)


    # submit Button
    subBottun2=Button(wd1,text="Submit",command=searchrecord,borderwidth=4,font="Times 12 bold",relief=RAISED,height=1,width=12)
    subBottun2.grid(row=3,column=1,columnspan=4)


    wd1.mainloop()

elif op==3:
    wd2=Tk()
    wd2.title('Withdrow money')
    HTitle3=Label(wd2,text='Withdrow money',fg="#06a099",font=("Arial",20))
    HTitle3.config(font=("Sylfaen", 30))
    HTitle3.grid(row=0,column=1,columnspan=4)


     # lable 
    cutname_L=Label(wd2,text="Customer name :",font=("Arial"),padx=10,pady=10)
    cutname_L.grid(row=1,column=0)

    cutAccountno_L=Label(wd2,text="Customer Account no. : ",font=("Arial"),padx=10,pady=10)
    cutAccountno_L.grid(row=1,column=2)

    Withmoney_L=Label(wd2,text="Enter money :",font=("Arial"),padx=10,pady=10)
    Withmoney_L.grid(row=2,column=0)

    Particular_L=Label(wd2,text="Particular :",font=("Arial"),padx=10,pady=10)
    Particular_L.grid(row=2,column=2)


    # Entry
    nm=StringVar
    parti=StringVar
    wdm=IntVar
    cutname_E=Entry(wd2,textvariable=nm,font=("Arial"))
    cutname_E.grid(row=1,column=1,padx=10,pady=10)

    cutAccountno_E=Entry(wd2,font=("Arial"))
    cutAccountno_E.grid(row=1,column=3,padx=10,pady=10)

    
    Withmoney_E=Entry(wd2,textvariable=wdm,font=("Arial"))
    Withmoney_E.grid(row=2,column=1,padx=10,pady=10)

    particular_E=Entry(wd2,textvariable=parti,font=("Arial"))
    particular_E.grid(row=2,column=3,padx=10,pady=10)

    

    # submit Button
    subBottun3=Button(wd2,text="Submit",command=customTransection,borderwidth=4,font="Times 12 bold",relief=RAISED,height=1,width=12)
    subBottun3.grid(row=3,column=1,columnspan=4)



    wd2.mainloop()


elif op==4:
    wd3=Tk()

    wd3.title('Deposit money')

    HTitle4=Label(wd3,text='Deposit money',fg="#06a099",font=("Arial",20))
    HTitle4.config(font=("Sylfaen", 30))
    HTitle4.grid(row=0,column=1,columnspan=4)


     # lable 
    cutname_L=Label(wd3,text="Customer name :",font=("Arial"),padx=10,pady=10)
    cutname_L.grid(row=1,column=0)
    
    cutAccountno_L=Label(wd3,text="Customer Account no. : ",font=("Arial"),padx=10,pady=10)
    cutAccountno_L.grid(row=1,column=2)

    Demosit_L=Label(wd3,text="Enter money :",font=("Arial"),padx=10,pady=10)
    Demosit_L.grid(row=2,column=0)

    Particular_L=Label(wd3,text="Particular :",font=("Arial"),padx=10,pady=10)
    Particular_L.grid(row=2,column=2)


    # Entry
    nm=StringVar
    parti=StringVar
    wdm=IntVar
    cutname_E=Entry(wd3,textvariable=nm,font=("Arial"))
    cutname_E.grid(row=1,column=1,padx=10,pady=10)

    cutAccountno_E=Entry(wd3,font=("Arial"))
    cutAccountno_E.grid(row=1,column=3,padx=10,pady=10)

    Particular_E=Entry(wd3,textvariable=parti,font=("Arial"))
    Particular_E.grid(row=2,column=3,padx=10,pady=10)
    
    Demosit_E=Entry(wd3,textvariable=wdm,font=("Arial"))
    Demosit_E.grid(row=2,column=1,padx=10,pady=10)


    # submit Button
    subBottun4=Button(wd3,text="Submit",command=customTransection,borderwidth=4,font="Times 12 bold",relief=RAISED,height=1,width=12)
    subBottun4.grid(row=3,column=1,columnspan=4)



    wd3.mainloop()

else:
    print('please select no.')


