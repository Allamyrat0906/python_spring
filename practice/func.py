# A=int(input("Enter the value: "))
# def PowerA3(A):
#     B=pow(A,3)
#     return B

# print("result :",PowerA3(A))


# A1=int(input("Enter the value: "))
# def PowerA3(A1):
#     B=pow(A1,3)
#     print("result: ", B)

# PowerA3(A1)



# def ShiftRight3(A,B,C):
#     temp=A
#     A=B
#     B=C
#     C=temp
#     return A, B , C 

# for triple in range(2):
#     A=int(input("Enter A value: "))
#     B=int(input("Enter B value: "))
#     C=int(input("Enter C value: "))
#     print(ShiftRight3(A,B,C))

K=int(input("Enter K  value: "))
def DigitCount(K):
    # logic if
    if K==0:
        return 1
    count=0
    sum=0
    # logic while
    while K!=0:
        count=count+1
        sum=sum+(K%10)
        K=K//10
    sumr=f"sum of digits {sum}"
    countr=f"Number of  digits: {count}"
    return sumr ,countr

print(DigitCount(K))





