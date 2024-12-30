#WRITE A PYTHON PROGRAM TO PRINT THE NO.OF VOWELS PRESENT IN THE USER ENTERED STRING
st=input("enter the string :")
Vowel_count=0
for i in st:
    if(i in('a','e','i','o','u','A','E','I','O','U')) :
        Vowel_count+=1
print("Vowel_count is :",Vowel_count)