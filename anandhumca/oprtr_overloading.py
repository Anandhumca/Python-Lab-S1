class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
    def __lt__(self,other):
        return self.area() < other.area()
print("rect1")
l1=int(input("enter length:"))
b1=int(input("enter breadth:"))
rect1=Rectangle(l1,b1)
print("\n")
print("rect2")
l2=int(input("enter length:"))
b2=int(input("enter breadth:"))
rect2=Rectangle(l2,b2)
print("\n")

if rect1<rect2:
    print("area of rect1 is smaller than rect2")
else:
    print("area of rect1 is greater than or equal to rect2")
