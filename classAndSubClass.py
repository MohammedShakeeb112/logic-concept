# # superClass or ParentClass or BaseClass
# class Person:
#     def display(self):
#         print('This is Super Class')
# # subClass or ChildClass or derivedClass
# class Employee(Person):
#     def show(self):
#         print('This is SubClass')

# emp = Employee()     #Creating object of SubClass
# emp.display()
# emp.show()

# per = Person()       #Creating object of SuperClass
# per.display()
# per.show()    #AttributeError: 'Person' object has no attribute 'show'


# # superClass
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display(self):
#         print('SuperClass name :', self.name, 'age :',self.age)
# # subClass
# class Employee(Person):
#     def show(self):
#         print('SubClass name :', self.name, 'age :', self.age)

# emp = Employee('Alpha', 26)             #creating a superClass Object
# emp.display()
# emp.show()
# print('Outside name : ', emp.name, 'age :', emp.age)

# #SuperClass
# class Person:
#     def __init__(self, per_name, per_age):
#         self.name = per_name
#         self.age = per_age
# #SubClass
# class Employee(Person):                                  #when subclass inherit       
#     def __init__(self, emp_name, emp_age, emp_salary):   #subclass the init_method overrides the superclass  init_method
#         self.salray = emp_salary
#         Person.__init__(self, emp_name, emp_age)         #prevent overrides 

# emp = Employee('Beta', 26, 50000)                       #creating object of superClass
# print(emp.name, emp.age, emp.salray)

# # superClass
# class Person:
#     def __init__(self, per_name, per_age):
#         self.name = per_name
#         self.age = per_age

#     def display(self):
#         print('name : ', self.name, 'age : ', self.age)

# # subClass
# class Employee:
#     def __init__(self, emp_name, emp_age, emp_salary):
#         self.salary = emp_salary
#         Person.__init__(self, emp_name, emp_age)
    
#     def show(self):
#         Person.display(self)
#         print('salary : ', self.salary)

# emp = Employee('Beta', 25, 25000)
# emp.show()


# # superClass
# class Person:
#     def __init__(self, per_name, per_age):
#         self.name = per_name
#         self.age = per_age

#     def display(self):
#         print('name:', self.name, 'age:', self.age)

# # subClass
# class Employee(Person):
#     def __init__(self, emp_name, emp_age, emp_salary):
#         self.salary = emp_salary
#         super().__init__(emp_name, emp_age)
    
#     def show(self):
#         super().display()
#         print('salary:', self.salary)

# emp = Employee('Beta', 25, 25000)
# emp.show()

# # inbuilt isinstance_method, issubclass_method
# # superClass
# class Person:
#     pass
# # subClass
# class Employee(Person):
#     pass

# per = Person()
# emp = Employee()
# print(isinstance(per, Person))
# print(isinstance(per, Employee))
# print(isinstance(emp, Person))
# print(isinstance(emp, Employee))
# print(issubclass(Person, Employee))
# print(issubclass(Employee, Person))


# EXECISE
# class Rectangle:                            #superClass
#     def __init__(self, length, breadth):
#         self.length = length
#         self.breadth = breadth
    
#     def area(self):
#         print(self.length * self.breadth)

# class Square(Rectangle):                    #subClass
#     def __init__(self, side):
#         self.side = side
#         super().__init__(side, side)
    
# s = Square(4)
# print(s.length)
# print(s.breadth)
# print(s.side)
# s.area()

# numbers = [str(x) for x in range(0, 10)]
# print(numbers)
# print([s for s in numbers if all(not int(ch) % 2 for ch in s)])
# print([int(ch) % 2 for ch in numbers])
# print([not int(ch) % 2 for ch in numbers])

# class Employee:
#     raise_amount = 0.26         #class variable
#     def __init__(self,fName,lName,pay):  #instance variable
#         self.fName=fName
#         self.lName=lName
#         self.email=fName+'.'+lName+'@co.in'
#         self.pay=pay
#     def get_fullName(self):     #class method
#         return '{} {}'.format(self.fName,self.lName)
#     def apply_raise(self):
#         self.pay=int(self.pay*self.raise_amount)

# class Developer(Employee):
    
#     raise_amount=2.25

#     def __init__(self, fName, lName, pay,prog_lang=None):
#         super().__init__(fName, lName, pay)  # we can use either supermethod or employee method for inherit from parent class 
#         # Employee.__init__(self,fName, lName, pay)  
#         self.prog_lang=prog_lang

# class Manager(Employee):
#     def __init__(self,fName,lName,pay,employees=None):
#         super().__init__(fName,lName,pay)
#         if employees is None:
#             self.employees=[]
#         else:
#             self.employees=employees
#     def add_emp(self,emp):
#         if emp not in self.employees:
#             self.employees.append(emp)
#     def remove(self,emp):
#         if emp in self.employees:
#             self.employees.remove(emp)
#     def print_emp(self):
#         for emp in self.employees:
#             print('=>',emp.get_fullName())

# dev1=Developer("Thomas", "Board", 17500, "Python")
# dev2=Developer("Alex", "Brait", 22600,"JavaScript")

# mgr_1=Manager('Rohan','Shety',25000,[dev1])
# # print(mgr_1.email)
# # mgr_1.print_emp()
# mgr_1.add_emp(dev2)
# # mgr_1.print_emp()
# mgr_1.remove(dev2)
# mgr_1.print_emp()

# print(isinstance(mgr_1, Manager))
# print(isinstance(mgr_1, Employee))
# print(isinstance(mgr_1, Developer))

# print(issubclass(Manager, Employee))           
# print(issubclass(Developer, Employee))         
# print(issubclass(Manager, Developer))          

#class method formation
class Employee:
    increment = 1.5     #class variable
    num_employee = 0    #class variable

    def __init__(self, fname, lname, salary):
        self.fname = fname          #instance variable
        self.lname = lname          #instance variable
        self.salary = salary        #instance variable
        Employee.num_employee += 1

    def increase(self):
        self.salary = int(self.salary * Employee.increment)
        return self.salary

    @classmethod
    def changeInc(cls, amount):
        cls.increment = amount
        
# print(Employee.num_employee)
# ram = Employee('Ram', 'Kumar', 10000)
# shyam = Employee('Shyam', 'Miller', 65000)
# print(Employee.num_employee)
# print(ram.salary)
# print(ram.increase())
# Employee.changeInc(4)
# print(ram.increase())

print('')