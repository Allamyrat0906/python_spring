# week=[" ", "Monday" , "Tuesday" , "Wednesday" , "Thursday" ,  "Friday" , "Saturday" , "Sunday"]
# get_day=int(input("enter the day's number: "))

# result=week[get_day]
# print("today is : " , result)



# FOR LOOP #1
# n=int(input("Enter N : "))
# k=int(input("Enter K : "))

# for i in range(n):

#     print("result ", k)

# n= int(input("enter N : "))
# sum=0
# for i in range(n):
#     sum=sum + pow((n+i),2)
#     print("result: ", sum)





# a=int(input("enter a: "))
# b=int(input("enter b: "))

# sum=0
# for i in range(a,b+1):
#     sum=sum+i
#     print("result ", sum)




print("\n\n\n\nWelcome to 'Sanly Bilim' education center!")
print("""
-------------- Our Course and their price   --------------
         
         SUBJECT                            PRICE
      ----------------------------------------------------
      1) Python web backend                4500 TMT (3 months)
      2) Web design                        4500 TMT (3 months)
      3) English                           1500 TMT (3 months)

""")

how_many_people_add=int(input("How many people to add: "))
subjects=["","Python web backend ", " Web design "," English" ]
filename=open('registration.txt', "w")
filename.write("--------------List of registered people.-------------------\n")
for i in range(1,how_many_people_add+1):
    #input section
    name=input("Enter your name:  ")
    surname=input("Enter your surname:  ")
    age=int(input("Enter your age:  "))
    phone=int(input("Enter your phone number: "))
    your_subject=int(input("""
             1) Python web backend 
             2) Web design 
             3) English   
                     selected number of subject :)  """ ))
    
    # write to text section
    filename.write(f"{i})")
    filename.write(str(f"\tName:   \t{name}\n"))
    filename.write(str(f"\tSurname:\t{surname}\n"))
    if 6<age<45:
        
        filename.write(str(f"\tAge:    \t{age}\n"))
    else:
       
        print("Unfortunately your age is not studying")
   
    new_phone=str(phone)
    if len(new_phone)==8:
        filename.write(str(f"\tPhone:  \t+993{phone}\n"))
    else:
        print("Your phone number is not Supported")
    filename.write(str(f"\tSubject:\t{subjects[your_subject]}\n"))
    filename.write("------------------------------------------------------------\n")
   
   
    filename.close()
    

    



