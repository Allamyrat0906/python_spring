# class Car:
#     object="BMW"

# value=Car()
# print(value)


# REAL CLASS

# class User:
#     def __init__(self,username,email):
#         self.username = username
#         self.email=email

# call=User("Allamyrat","allamyrat@gmail.com")

# call1=call.username
# call2=call.email

# # WE CALL CLASS THIS WAY EFFECTively
# print(call1)
# print(call2)

# we call this waY 
# print(call.username)
# print(call.email)



# class Car:
#     def __init__(self,car_1,car_2):
#         self.car_1 = car_1
#         self.car_2 = car_2

# get_car=Car("BMW","AMG")

# print(get_car.car_1)

# class Administrator():
#     def __init__(self,username,password):
#         self.username = username
#         self.password = password

#     def __str__(self):
#         return f" Enter your username {self.username}  \
#         and password {self.password}"
    
#     def getName(self):return f" Enter your username use function {self.username}  \
#         and password {self.password}"


    
# get_Admin=Administrator("Allamyrat", "python")

# # we create own function get string 
# get_function=get_Admin.getName()
# print(get_function)

# # we use str function in class
# print(get_Admin)

# class Person:
#     def __init__(self,name,age=12):
#         self.name=name
#         self.age=age
      

#     def printName(self,):
#         return f" Hi  I am {self.name} and  {self.age} and "
    
# get_Person=Person("Allamyrat")
# value=get_Person.printName()
# print(value)



class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
del p1.myfunc()

print(p1)