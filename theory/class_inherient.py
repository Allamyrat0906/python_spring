# class Person:
#     def __init__(self,firstname,lastname):
#         self.firstname = firstname
#         self.lastname = lastname

#     def printname(self):
#         print(self.firstname , self.lastname)


# class Student(Person):
#     pass
    

# std_name=Student("Allamyrat","Annayev")
# std_name.printname()



# class Person:
#     def __init__(self,firstname,lastname,gender ):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.gender=gender
     

#     def printname(self):
#         print(self.firstname , self.lastname , self.gender)


# class Student(Person):
#     def __init__(self, fname, lname, gender="Male"):
#         Person.__init__(self, fname, lname, gender)

# value_s=Student("Mike ", "Tison" )
# value_s.printname()        
    

# firstname=input("First Name: ")
# lastname=input("Last Name: ")

# class Person:
#     def __init__(self,firstname,lastname):
#         self.firstname = firstname
#         self.lastname = lastname

#     def printname(self):
#         print(self.firstname , self.lastname)

# class Student(Person):
#     def __init__(self, firstname, lastname):
#         super().__init__(firstname,lastname)
#         self.finelYear=2024

# super_v=Student(firstname,lastname)
# super_v.printname()

# get_out=super_v.finelYear
# print("Super Clas : " , get_out)
   

# class Example:
#     def __init__(self):
#         self.name="Allamyrat"

# c=Example()
# print(c.name)


# firstname=input("First Name: ")
# lastname=input("Last Name: ")
# finalYear=int(input("enter the your final year: "))

# class Person:
#     def __init__(self,firstname,lastname):
#         self.firstname = firstname
#         self.lastname = lastname

#     def printname(self):
#         print(self.firstname , self.lastname)

# class Student(Person):
#     def __init__(self, firstname, lastname,finalYear):
#         super().__init__(firstname,lastname)
#         self.finelYear=finalYear

# super_v=Student(firstname,lastname, finalYear)
# super_v.printname()

# get_out=super_v.finelYear
# print("fINAL yeAR : " , get_out)


# firstname=input("First Name: ")
# lastname=input("Last Name: ")
# finalYear=int(input("enter the your final year: "))

# class Person:
#     def __init__(self,firstname,lastname):
#         self.firstname = firstname
#         self.lastname = lastname

#     def printname(self):
#         print(self.firstname , self.lastname)

# class Student(Person):
#     def __init__(self, firstname, lastname,finalYear):
#         super().__init__(firstname,lastname)
#         self.finelYear=finalYear
        

#     def welcomeClass(self):
#         print(f"Welcome {self.firstname} and {self.lastname} \
#               granduation year {self.finelYear}")
        
# super_v=Student(firstname,lastname, finalYear)
# super_v.printname()

# get_out=super_v.finelYear
# print("fINAL yeAR : " , get_out)

# super_v.welcomeClass()

# class Vehicle:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Move!")

# class Car(Vehicle):
#   pass

# class Boat(Vehicle):
#   def move(self):
#     print("Sail!")

# class Plane(Vehicle):
#   def move(self):
#     print("Fly!")

# car1 = Car("Ford", "Mustang") #Create a Car object
# boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
# plane1 = Plane("Boeing", "747") #Create a Plane object

# for x in (car1, boat1, plane1):
#   print(x.brand)
#   print(x.model)
#   x.move()

# print()


# def myfunc():
#   x = 300
#   def myinnerfunc():
#     print(x)
#   myinnerfunc()

# myfunc()

# x = 300

# def myfunc():
#   x=24
#   print(x)

# myfunc()

# print(x)


# global x
# x=30

# def myfunc():
#   #global 
#   x=90
#   print(x)

# myfunc()




# def myfunc1():
#   x = "Jane"
#   def myfunc2():
    
#     x = "hello"
#     return x
#   myfunc2()
#   return x

# print(myfunc1())



# x = min(5, 10, 25,5)
# y = max(5, 10, 25,5)

# print(x)
# print(y)



# import json

# # some JSON:
# x = '{ "name":"John", "age":30, "city":"New York"}'

# # parse x:
# y = json.loads(x)

# # the result is a Python dictionary:
# print(y["age"])



# import json

# # a Python object (dict):
# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }

# # convert into JSON:
# y = json.dumps(x)

# # the result is a JSON string:
# print(y)



# import camelcase

# c = camelcase.CamelCase()

# txt = "lorem ipsum dolor sit amet"

# print(c.hump(txt))

# #This method capitalizes the first letter of each word.

# x=9
# y="ss"
# try:
#   print(x+y)
# except NameError:
#   print("Variable x is not defined")
# except TypeError:
#   print("we dont add string and intger")
# except:
#   print("Something else went wrong")

# c=input("enter :")
# print(c)
C=raw_input("Please: ")
print(C)