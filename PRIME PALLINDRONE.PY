#WRITE A PYTHON PROGRAM TO PRINT TO CHECK WETHER USER ENTERED INTEGER IS A PRIME PALLINDRONE OR NOT
#PROGRAM
num= int(input("enter the integer value:"))
Reversed_num=0
rem=0
Temp=num
while(num!=0):
    rem=num%10
    Reversed_num=Reversed_num*10+rem
    num//=10
    #for i in range(1,num+1):
    if(Temp==Reversed_num) and (num%i==0):
          print(Temp," is a prime pallindrone number")
    else:
        print(Temp,"is not a  prime pallindrome")