'''write a python program to read the year as input from user & check 
wheter it is leap year or non leap year'''
year= int(input("enter a year:"))
if( year%4==0 and year%100==0)or year%400:
    print(year,"the year is leap year")
else:
    print(year,"the year is not leap year")