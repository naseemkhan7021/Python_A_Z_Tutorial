import shape1 as s  #shape1 filename  and shape class 
class triangle(s.shape): #derived class triangle and inherits base class shape
    def area(self):
        a=s.shape.area_triangle(self) #call function of base class
        print("area of triangle=",a)
class circle(s.shape): # derived class circle  inherits base class shape which stored in shape1 file
    def area(self):
        print("Area of circle = ",s.shape.area_circle(self))
class rectangle(s.shape):
    def area(self):
        print("Area of rectangle = ",s.shape.area_rectangle(self))

#main program
tr=triangle()
tr.area()
c=circle()
c.area()
re=rectangle()
re.area()

