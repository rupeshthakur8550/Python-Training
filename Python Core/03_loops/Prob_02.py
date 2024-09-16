n = int(input("Enter no to calculate sum of even: "))

sum = 0;
for num in range (1, n + 1):
    if(num & 1 == 0):
        sum += num
print("Sum of Even numbers is: ", sum)