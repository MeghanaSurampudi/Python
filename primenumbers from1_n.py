#write a python program to print from 1 to n numbers
#PROGRAM
num=int(input("enter the integer number:"))
for i in range(2,num+1):
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        print(i)
        
