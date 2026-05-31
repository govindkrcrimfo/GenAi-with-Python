# Just like Java, Python supports the four main OOP principles:
# Encapsulation
# Inheritance
# Polymorphism
# Abstraction

#Constructor (__init__)
class Student:

    school='NEPS'   #class variable

    def __init__(self,id , name):
        self.id=id
        self.name=name

    # class method - cls parameter is mandatory for class method
    @classmethod
    def getSchool(cls):
        return cls.school
    
    # static method 
    @staticmethod
    def info():
        print("This is static method inside student class")
    
    def getId(self):
        return self.id
    def getName(self):
        return self.name
    

#object 
s=Student(1,"Govind")
print(s.getId())
print(s.getName())

#class method call
print(Student.getSchool())

#static method call
Student.info()