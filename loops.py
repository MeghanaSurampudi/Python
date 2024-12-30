a=int(input("enter a number"))
for i in range(1,a+1):
    print(i)
print("************************")
num=int(input("enter the integer value :"))
if(num%2==0):
    print(num,"is even")
else:
    print(num, "is odd")
result="even" if(num%2==0) else "odd number"
print(result)
print("*******************************")
num=int(input("enter the integer value :"))
if(num%3==0) and num%5==0:
    print(num,"is divisiable by 3,5")
else:
    print(num, "is not divisiable by 3,5")
result="even" if(num%3==0)and num%5==0 else "not divisiable"
print(result)