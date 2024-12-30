#write python program to read the student name and scores of  3 subjects & print the student report card
#PROGRAM
print("___________________________")
print("Student Report Card :")
print("_________________________")
name=str(input("Student Name :"))
Sub1=int(input("Subject1 Score :"))
Sub2=int(input("Subject2 Score :"))
Sub3=int(input("Subject3 Score :"))
Total=Sub1+Sub2+Sub3
print("Total: ",Total)
Average=Total/3
print("Average: ",Average)
if (Average>=90):
     print("**Congratulations your qualified in 1st class** ")
elif (Average>=75):
     print("**Congratulations your qualified in 2nd class** ")    
elif (Average>=60): 
     print("**Congratulations your qualified in 3rd class** ")    
else:
     print("**Your not qualified in the examinations** ")     