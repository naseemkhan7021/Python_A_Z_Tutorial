class student:  #base class student
    def __init__(self): #constructor function
        self.__rno=int(input("enter rollno."))
        self.__name=input("enter name")
        self.__age=int(input("enter age"))
        self.__city=input("enter city")
    def showstudent(self):
        print("rollno. : ",self.__rno)
        print("name : ",self.__name)
        print("age : ",self.__age)
        print("city : ",self.__city)
class marks: #here marks  base class 
    def __init__(self) :#constructor function
        self.p=float(input("enter marks of physics"))
        self.c=float(input("enter marks of chemistry"))
        self.m=float(input("enter marks of maths"))
    def showmarks(self):
        print("marks of Physics : ",self.p)
        print("marks of chemistry : ",self.c)
        print("Marks of maths : ",self.m)
class result(student,marks):  #here result derived class and inherits base class student and base class marks
    def __init__(self):  #constructor function
        super().__init__() #call constructor function of base class student
        marks.__init__(self)
    def compute(self):
        t=self.p+self.c+self.m
        per=t*100/300
        print("\n total marks : ",t)
        print("\n Percent : ",per)
        
        
#main program
res=result()
res.showstudent()
res.showmarks()
res.compute()

        
    
