#write a python program to print the summation of the digits present in the user entered integer!!!
a=int(input("enter integer value"))
sum_digits=0
remainder=0
while(a!=0):
    remainder=a%10
    sum_digits=sum_digits+remainder
    a=a//10
print("the summation is",sum_digits)