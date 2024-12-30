#write a python program to read the input for principleamount ,rate of interest,time to calculate the simple interest
#********PROGRAM***********
p=int(input("Enter the principle amount : "))
t=int(input("Enter the time to be taken"))
r=int(input("Enter the rate of interest :"))
simple_interest=p*t*r/100
print("THE SIMPLE INTEREST IS :",simple_interest)