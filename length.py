#write a python program to print the number of even digits present in the user entered integer!!!
#write a python program to print number of odd digits present in the user entered integer

a=int(input("enter integer value:"))
evDGcount=0
rem=0
while(a!=0):
    rem=a%10
    if(rem%2==0):
        evDGcount+=1
    a=a//10
print("number of even digits are",evDGcount)
