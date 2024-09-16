num = int(input("Enter a number to calculate factorial: "))

fact = 1
while(num > 0):
    fact *= num
    num -= 1

print(f"Factorial of a number is : {fact}")