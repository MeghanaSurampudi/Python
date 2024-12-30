n=int(input("enter month"))
if (n==1 or n==3 or n==5 or n==7 or n==8 or n) :
    print("31 days")
elif(n==2):
    print("28 or 29 days")
elif (n==4 or n==6 or n==9 or n==11) :
    print("30 days")
else:
    print("invalid month")
