#write a python program to print the reversed number of user entered number without using built-in functions;
a= int(input("enter the integer value:"))
Reversed_a=0
rem=0
while(a!=0):
    rem=a%10
    Reversed_a=Reversed_a*10+rem
    a//=10
print("reversed number:",Reversed_a)