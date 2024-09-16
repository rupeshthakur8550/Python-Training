arr = ["apple", "banana", "orange", "apple", "mango"]

unique_arr = set()

for item in arr:
    if(unique_arr.__contains__(item)):
        print(item)
        break
    unique_arr.add(item)

