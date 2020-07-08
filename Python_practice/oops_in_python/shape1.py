class shape : #base class
    def area_triangle(self):
        b=int(input("enter base"))
        h=int(input("enter height"))
        return b*h/2
    def area_circle(self):
        r=int(input("enter radius"))
        return 3.14*r*r
    def area_rectangle(self):
        l=int(input("enter length"))
        w=int(input("enter width"))
        return l*w

        
c=shape()
a=c.area_triangle
b=c.area_circle
c=c.area_rectangle
print(a)
