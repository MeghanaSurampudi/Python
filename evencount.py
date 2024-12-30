a= int(input("enter a value"))
evcount=0
odcount=0
for i in range(1, a+1):
    if(i%2==0):
        evcount=evcount+1
    else:
        odcount=odcount+1
print("even numbers from 1to n are:",evcount)
print("odd numbers from 1to n are:",odcount)
