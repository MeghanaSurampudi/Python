str= str(input("Enter the string"))
if str.isalnum():
    print("the string is algebraic number")
elif str.isalpha():
    print("the string is alphabet")
elif str.isdigit():
    print("it is digit")
elif str.isnumeric():
    print("it is numerals")
else:
    print("does not belong to string")