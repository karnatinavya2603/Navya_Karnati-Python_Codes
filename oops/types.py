#Single Inheritence 
class animal:
    def sound(self):
        print("Animals Makes sound")
class dog(animal):
    def bark(self):
        print("Dogs Bark")
d = dog()
d.sound()
d.bark()
#Multiple Inhertence 
class Father:
    def skill1(self):
        print("Driving")
class Mother:
    def skill2(self):
        print("Cooking")
class child(Father,Mother):
    pass 
d= child()
d.skill1()
d.skill2()
#MultilevelInheritence 
class grandfather:
    def land(self):
        print("Ownd Land")
class Father(grandfather):
    def house(self):
        print("owns house")
class child(Father):
    def car(self):
        print("Owned a car")
o = child()
o.land()
o.house()
o.car()
#Hirechiral Inheritence 
class animal:
    def eat(self):
        print("Animals eat food")
class dog(animal):
    def bark(self):
        print("Dog is Barking")
class cat(animal):
    def meow(self):
        print("cat meows")
b = dog()
c = cat()
b.bark()
c.meow()
#Hybrid Inheritence
class A:
    def method1(self):
        print("Class A")
class B(A): 
    def method2(self):
        print("Class B")
class C(A):
    def method3(self):
        print("Class C")
class D(B,C):
    def method4(self):
        print("Class D")
d = D()
d.method1()
d.method2()
d.method3()
d.method3()
#Single Inheritence
class Vehicle:
    def start(self):
        print("Vehicle starts")

class Car(Vehicle):
    def drive(self):
        print("Car is driving")

c = Car()
c.start()
c.drive()
#Multiple Inheritence 
class Subject:
    def subject_name(self):
        print("Subject: Mathematics")

class Experience:
    def years(self):
        print("Experience: 5 years")

class Teacher(Subject, Experience):
    def teacher_name(self):
        print("Teacher: Ramesh")

t = Teacher()
t.subject_name()
t.years()
t.teacher_name()
#Multilevel Inheritence 
class Company:
    def company_name(self):
        print("Company: ABC Pvt Ltd")

class Employee(Company):
    def employee_id(self):
        print("Employee ID: 102")

class Manager(Employee):
    def department(self):
        print("Department: IT")

m = Manager()
m.company_name()
m.employee_id()
m.department()
#Hierarchical Inheritence 
class Shape:
    def draw(self):
        print("Drawing shape")

class Circle(Shape):
    def circle(self):
        print("This is a circle")

class Rectangle(Shape):
    def rectangle(self):
        print("This is a rectangle")

c = Circle()
r = Rectangle()

c.draw()
c.circle()

r.draw()
r.rectangle() 
#Hybrid Inheretence
class Device:
    def power_on(self):
        print("Device power ON")

class Phone(Device):
    def call(self):
        print("Making a call")

class Camera(Device):
    def click(self):
        print("Taking photo")

class Smartphone(Phone, Camera):
    def internet(self):
        print("Using internet")

s = Smartphone()
s.power_on()
s.call()
s.click()
s.internet()
#Encapsulation Example 
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks   

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.__marks)

s = Student("Navya", 90)
s.display()