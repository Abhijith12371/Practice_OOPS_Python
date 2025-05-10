# classes
# objects
# class variables
# object varabiles
# instance variables

# magic or dender methods
# constructors
# inheritance
#     multiple inheritance
#     single inheritance
#     hirarichal inheritance



class CSD:

    def __init__(self,n1,n2): #the instance of the object is represented by self
        self.n1=n1
        self.n2=n2

    def display(self):
        print(f"Hi I am {self.n1} studying {self.n2}")
    def __str__(self):
        return "This is a dunder or magic method used to overwrite the str method"
    def __add__(self,other):
        return self.n1+other.n1+other.n2+self.n2
    def muti_name(self,*number):
        self.number=number
        return sum(number)

    
obj=CSD(1,2)
obj1=CSD(3,2)


print(obj.muti_name(1,2,3,4,5,6,7,8,9))




create a class even or odd which takes a list of numbers as input and classifies into even or odd


class evenOdd:
    even=[]
    odd=[]
    def __init__(self,*numbers):
        self.numbers=numbers
    def classify(self):
        for i in self.numbers:
            if i%2==0:
                evenOdd.even.append(i)
            else:
                evenOdd.odd.append(i)
        print(evenOdd.even)
        print(evenOdd.odd)
obj=evenOdd(1,2,3,4,5,6,7,8,9)

obj.classify()



class Things:
    def __init__(self,*things):
        self.things=things
    def display(self):
        print(f"The things are   {self.things}")


class Abhijith(Things):
    def show(self):
        print("this is a function")
    def display(self):
        return super().display()
class Karthikeya(Things):
    pass
class XYZ(Karthikeya):
    pass
    
obj=Abhijith("Abhijith","KK","Dwarakesh","LSY")


obj.display()


class numbers:
    def __init__(self,*numbers):
        self.numbers=numbers
    def __getitem__(self,index):
        return self.numbers[index]
    def __setitem__(self,index,value):
        a=list(self.numbers)
        a[index]=value
        return a

obj=numbers(1,2,2,3,4,5,6,7)

print(obj.__getitem__(3))
print(obj.__setitem__(0,0))


class demo:
    def __init__(self,name):
        self.name=name
    def __len__(self):
        return len(self.name)
    
obj=demo("ABhijith")
print(len(obj))
print(hasattr(obj,"name"))
print(getattr(obj,"name"))
setattr(obj,"name","kk")
print(obj.name)


create a class student which stores all the subject marks of the student

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        d={}
        d[self.name]=self.marks
        print(d)
name=input("Enter the name: ")
marks=list(map(int,input().split()))


obj=Student(name,marks)



class Circle:
    pi=3.14
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return Circle.pi*self.radius*self.radius
    def perimeter(self):
        return 2*Circle.pi*self.radius
cir=Circle(6)

print(cir.area())
print(cir.perimeter())



class Animal:
    def make_sound(self):
        print("I am barking...")
class DOG(Animal):
    def make_sound(self):
        print("Dog is barking...")
class Cat(Animal):
    def make_sound(self):
        print("Cat cannot make a sound...")


dg=DOG()
dg.make_sound()

ct=Cat()

ct.make_sound()



a=input() #153
sum=0
org=int(a)
for i in a:
    sum+=int(i)**3
if sum==org:
    print("YES")
else:
    print("NO")


a=input()

if a==a[::-1]:
    print("yes")
else:
    print("no")


