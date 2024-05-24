def print_two(*args):
    args1,args2=args
    print(f"args1 {args1} ,args2 : {args2}")

def print_two_again(arg1,arg2):
    print(f"args1 {arg1} ,args2 : {arg2}")

def print_one(arg1):
    print(f"args1 {arg1}")

def print_none():
    print("I got nothin")

print_two('ZED', "SHaw")
print_two_again("Zed", "SHaw")
print_one("First")
print_none()
