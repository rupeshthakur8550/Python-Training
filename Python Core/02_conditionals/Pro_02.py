age = int(input("Enter age to get the price of ticket : "))
day = input("Enter day to watch movie : ")
price = 12 if age >= 18 else 8

if(day == "Wednesday"):
    price -= 2

print(f"Ticket price for movie is {price}")

