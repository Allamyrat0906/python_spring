# list 

# fruits=["apple", "orange","banana","watermelon"]
# print(len(fruits))
# print(fruits[0])
# print(fruits[-1])
# print(fruits[2])

# drinks=["cola","limonad"]
# list_value=[12,"Hello",True,1.5,12]

# print(list_value)
# print(type(drinks))
# print(type(list_value))

# fruits=("apple", "orange","banana","watermelon")

# print(fruits)
# print(type(fruits))

# # convert to list
# print("--"*10)

# t_to_l=list(fruits)
# print(t_to_l)
# print(type(t_to_l))

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:])

# if "apple fruit" in thislist:
#     print("yes apple here")
# else:
#     print("no")

# thislist = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

# new_value=list(thislist)
# new_value[0]="Other frasdiuyg"
# print(new_value)


# #thislist.insert(2,"test")

# print(thislist.index("mango"))
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# thislist.append("test")
# print(thislist)
# food=[]
# while True:
#     add_value=input("enter value: ")
#     food.append(add_value)
#     print(food)

# motorbike=["motor1","motor2"]
# car=["BMW ","AMG","FORD"]

# car.extend(motorbike)

# print(car)

# REMOVE()
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# thislist.remove("apple")

# print(thislist)

# pop()
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# thislist.pop(0)
# print(thislist)

#del ()
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# del thislist[1:5]
# print(thislist)

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# thislist.clear()
# print(thislist)

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

# for x in thislist:
#     print(x)


# for test in  "Ayhan":
#     print(test)

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

# for single in range(len(thislist)):
#     print(single)

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# i=0
# while len(thislist)>i:
#     print(thislist)
#     i+=1

# thislist = [ "banana",  "orange", "kiwi", "melon","cherry", "mango","apple",]
# thislist.sort()
# print(thislist)
# thislist.sort(reverse=True)
# print(thislist)



# number=[52,23,2,43,4]
# number.sort()
# print(number)


# thislist = ["APPLE", "banana", "CHerry", "orange", "kiwi", "melon", "mango"]

# thislist.sort(key=str.lower)
# print(thislist) 


# thislist = ["Banana"]

# #thislist.sort(key = str.lower)
# thislist.lower()
# print(thislist)


# thislist = ["banana", "Orange", "Kiwi", "cherry"]

# number=[1,3,4,4]

# drink=["cola",'pepsi']

# new=thislist+number+drink
# print(new)


thislist = ["banana", "Orange", "Kiwi", "cherry"]

drink=['cola','pepsi','limond','tut','akar']

for x in drink:
    thislist.append(x)

    print(thislist)

