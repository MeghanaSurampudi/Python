 #write a python program to swap two numbers by talking the input from the user!!
#PROGRAM
#without using third variable
a= int(input("enter the first number: "))
b= int(input("enter the second  number: "))
print("Before swapping")
print("NUM1=",a)
print("NUM2=",b)
a,b=b,a
print("after swapping:")
print("NUM1=",a)
print("NUM2=",b)
#using third variable
a= int(input("enter the first number: "))
b= int(input("enter the second  number: "))
print("Before swapping")
print("NUM1=",a)
print("NUM2=",b)
temp=a
a=b
b=temp
print("after swapping:")
print("NUM1=",a)
print("NUM2=",b)
#using arthmetic operators
a= int(input("enter the first number: "))
b= int(input("enter the second  number: "))
print("Before swapping")
print("NUM1=",a)
print("NUM2=",b)
a=a+b
b=a-b
a=a-b
print("after swapping:")
print("NUM1=",a)
print("NUM2=",b)