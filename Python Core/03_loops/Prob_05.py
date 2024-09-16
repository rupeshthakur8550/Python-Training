str = input("enter string: ")

for char in str:
    if str.count(char) == 1:
        print(char)
        break

 