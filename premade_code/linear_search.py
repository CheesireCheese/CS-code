number = ["a", "b", "c", "d", "e"]
target = input("Enter name to find ")
Found = False
Index = 0
for i in range(len(number)): #loop to search for the target in the list
    if number[i] == target:
        Found = True
        Index = i
        break

if Found:
    print("name found, index ", Index)
else:
    print("name not found")