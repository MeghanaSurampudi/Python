#Write a python program to check whether the user entered number is prime or not!!!
#PROGRAM
num= int(input("enter the integer number :"))
count=0
for i in range(1,num+1):
    if(num%i==0):
        count+=1
if(count==2):
    print("prime number")
else:
    print("not a prime number")
print("***********type2*************")
for i in range(2,num):
    if(num%i!=0):
        print("not a prime number")
        break
    else:
        print("prime number")
        break
