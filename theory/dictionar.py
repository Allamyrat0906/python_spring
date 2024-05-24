# car={
#     "brand":"BMW",
#     "Model":"X6",
#     "year":2022,
#     }

# print(car["brand"])



# en_to_tm={
#     "apple":"alma",
#     "orange":"pyrtykal",
#     "chery":"ulje",
#     "chery":"uljeler",
#     "limon":"limanoad",

# }

# print(en_to_tm["chery"])
# print(len(en_to_tm))
# #value=input("enter your word:  ")


# car={
#     "brand":"BMW",
#     "Model":"X6",
#     "isthebestcar":True,
#     "year":[2012,2013,2014]
#     }

# print(car["isthebestcar"])
# print(car["year"])

# thisdict = dict(name="john", surname="carter")
# print(thisdict)

# car={
#     "brand":"BMW",
#     "Model":"X6",
#     "year":2022,
#     }

#x=car["brand"]
# x=car.get("Model")
# print(x)
# cars=[]
# new=car.keys()
# for i in new:
#     cars.append(i)
# print(cars)





# car["color"]="white"
# print(car.keys())


# car["year"]=2002
# new=car.values()
# print(new)


# if "brand" in car:
#     print("yes")
# else:
#     print("no")


# new=car.update({"year":2012})
# print(car)
# car["color"]="green"

#new=car.pop("brand")
# car.popitem()

# print(car)

#del car["brand"]
# car.clear()
# print(car)


# for i in car:
#     print(car[i])

# for i ,x in car.items():
#     print(i,x)

# car={
#     "brand":"BMW",
#     "Model":"X6",
#     "year":2022,
#     }

# client={
#     "user1":{
#         "username":"Item1",
#         "email":{
#             "email1":"itmem1@gmail.com",
#             "email2":"itmem2@gmail.com",
#         }
#     },
#     "user2":{
#         "username":"Item2",
#         "email":"item2@example.com",
#     },
#     "user3":{
#         "username":"Item3",
#         "email":"item3@example.com",
#     },
# }
# new=client["user1"]["email"]["email1"]
# print(new)

import random
print("welcom chker game!!")
print('''
            Game Rules:
            choose one door and entered 
            door1 > 1
            door2 > 2
            door3 > 3
            
''')

door=int(input("Which door do you want to ?? "))

if door==1:
    print("Please enter random number between 1 and 10 ? ")
    ran=int(input("Enter a random number: "))
    rabdomnum=random.randint(1,10)
    
    if ran==rabdomnum:
        print("Urrra You are genuius")
    else:
        print(f"I remember this number:  {rabdomnum} \n and you get {ran}")
        print("You lost : Try again")

if door ==2:
    print("welcome know capital of country game!!")
    country={
        "TKM":"ashgabat",
        "USA":"washington",
        "RUS":"moscow",
        "UAE":"abu dabi",
        "GRM":"berlin",
    }
    countries=["",]
    capitalies=["",]
    for c in country.keys():
        countries.append(c)
    for cp in country.values():
        capitalies.append(cp)
    capran=random.randint(1,5)
    country_list=countries[capran]
    print(f"okey do you know capital of this country: {country_list}")
    capital_input=input("Write Answer:  ")
    if capital_input==country[country_list]:
        print(f" yes you are right : Capital of {country_list} >> ({capital_input})")
    else:
        print(f"No you are wrong\n \tanswer: ({country[country_list]})")
        


