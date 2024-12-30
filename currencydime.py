#write a python program to read the amount as input from the user & print the number of notes required in indian currency dimensions!!!
amount = int(input("Enter the amount: "))
denominations = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
n2000 = amount // 2000
amount %= 2000
n500 = amount // 500
amount %= 500
n200 = amount // 200
amount %= 200
n100 = amount // 100
amount %= 100
n50 = amount // 50
amount %= 50
n20 = amount // 20
amount %= 20
n10 = amount // 10
amount %= 10
n5 = amount // 5
amount %= 5
n2 = amount // 2
amount %= 2
n1 = amount // 1
amount %= 1
print("2000 Rs ------------------>", n2000)
print("500 Rs-------------------->", n500)
print("200 Rs ------------------->", n200)
print("100 Rs ------------------->", n100)
print("50 Rs -------------------->", n50)
print("20 Rs -------------------->", n20)
print("10 Rs -------------------->", n10)
print("5 Rs --------------------->", n5)
print("2 Rs --------------------->", n2)
print("1 Rs --------------------->", n1)
