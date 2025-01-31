#1
class String:
    def getstring(self):
        self.sentence=input("Sentense:")
    def printstring(self):
        print("With upper case:"+self.sentence.upper())
        
mystring=String()
mystring.getstring()
mystring.printstring()

#2
class Shape():
    def area(self):
        return 0
class Square(Shape):
    def __init__(self,length):
        self.length=length
    def area(self):
        return self.length ** 2
a = float(input("a:"))
mysquare=Square(a)
print("sharshy audany:",mysquare.area())
myshape=Shape()
print("Basqa:",myshape.area())

#3
class Shape:
    def area(self):
        return 0
class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
length = float(input("Length: "))
width = float(input("Width: "))
audan=Rectangle(length,width)
print("Area of the rectangle:",audan.area())