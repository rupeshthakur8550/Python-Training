marks = int(input("Enter marks to know your grade : "))

if(marks < 0 and marks > 100):
    print("Wrong Input")
elif(marks < 60):
    print("Grade F")
elif(marks < 69):
    print("Grade D") 
elif(marks < 79):
    print("Grade C")
elif(marks < 89):
    print("Grade B") 
else:
    print("Grade A")