class Student:
    college_name = "SSM"
    name = "anonymous" #class attribute
    #name = "Karan Kumar"
    def __init__(self,name,marks):
        
        self.name= name #object attribute
        self.marks = marks
        
        print("Adding new student in Database")
    

s1 = Student("Sadaf",12)
print(s1.name)
print(s1.marks)
print(s1.college_name)
print(Student.college_name)
s2 = Student("Radha",13)
print(s2.name,s2.marks)
s3 = Student() #confusion
print(s3.name)
class Car:
    color = "Blue"
    brand = "mercedes"
car1 = Car()  
print(car1.color) 
print(car1.brand)
car2 = Car()
#The self parameter is a referance to the current instance of the class,
#and is used to access variables that belong to the class
#default constructor: Only self parameter is passed
#parameterized constructor: other parameters are also passed
