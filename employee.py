'''Write a python program to read Employee name, salary, designation,special allowances,bonus as input from the input user
i)gross monthly salary(salary +special allowances)
ii)gross annual salary (gross monthly salary salary x 12+ bonus)
iii)calculate the taxable income
    if salary>500000-----15% tax
    salary>400000------10% tax
    salary >100000 to 30000------->2% tax'''
name=str(input("Name: "))
designation=str(input("Designation: "))
salary=int(input("Salary : "))
Sp_allow=int(input("The Special allowances : "))
Bonus=int(input("The monthly BONOUS : "))
gms= salary+Sp_allow
g_a_s=gms*12+Bonus
print("****The tax for the annual income**** ")
if salary>=500000:
    Annualtax=g_a_s*15/100
    g_a_s=g_a_s-Annualtax
    print("The annual income after tax : ",g_a_s)
elif salary>=400000:
    Annualtax=g_a_s*10/100
    g_a_s=g_a_s-Annualtax
    print("The annual income after tax : ",g_a_s)
elif(salary>=range(100000,300000)) :
    Annualtax=g_a_s*2/100
    g_a_s=g_a_s-Annualtax
    print("The annual income after tax : ",g_a_s)
else:
    print("your not eligible for tax")