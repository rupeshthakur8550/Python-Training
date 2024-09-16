arr = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

count = 0
for i in arr:
    if(i > 0):
        count += 1
    
print(f"List contains {count} positive numbers")