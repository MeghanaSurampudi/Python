#odd numbers
a=int(input("enter a number"))
for i in range(1,a+1):
    if(i%2!=0):
        print(i)

#multiplication table
a=int(input("enter a number"))
print("multiplication  of table",a,":")
for i in range(1,11):
        print(a,"X",i,"=",a+i)