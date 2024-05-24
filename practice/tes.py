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
    if 6<age<45:        
        pass
    else:       
        print("Unfortunately your age is not studying")
        break

    phone=int(input("Enter your phone number: +993"))
    while True:
        try:            
            if len(str(phone))==8:
                break
            else:
                phone=int(input("Enter your phone number Again: +993"))
        except ValueError:
            print("Your phone number is not a valid integer.") 
    your_subject=int(input("""
             1) Python web backend 
             2) Web design 
             3) English   
                     selected number of subject :)
    """ ))
    
    # write to text section
    filename.write(f"{i})")
    filename.write(str(f"\tName:   \t{name}\n"))
    filename.write(str(f"\tSurname:\t{surname}\n"))
    filename.write(str(f"\tAge:    \t{age}\n"))
    filename.write(str(f"\tPhone:  \t+993{phone}\n"))
    filename.write(str(f"\tSubject:\t{subjects[your_subject]}\n"))
    filename.write("------------------------------------------------------------\n")
   
   
filename.close()
    