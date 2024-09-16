import math
n = int(input("Enter a number: "))

for i in range (2, int(math.sqrt(n)+ 1)):
    if(n % i == 0):
        print(f"{n} is Not a Prime number")
        break
else:
    print(f"{n} is a Prime number")

