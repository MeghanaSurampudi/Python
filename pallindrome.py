#write a python program to check whether the user entered number is a pallindrone number or not
a= int(input("enter the integer value:"))
Reversed_a=0
rem=0
Temp=a
while(a!=0):
    rem=a%10
    Reversed_a=Reversed_a*10+rem
    a//=10
if(Temp==Reversed_a):
    print(Temp,"pallindrone number")
else:
    print(Temp,"is not a pallindrome")
