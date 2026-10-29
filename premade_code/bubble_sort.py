my_list = [45, 32, 78, 12, 99]
n = len(my_list)
for i in range(n):
    swapped = False
    for j in range(0, n - i - 1):
        if my_list[j] > my_list[j + 1]:
            my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
            swapped = True
    if not swapped:
        break

print("Sorted list is:", my_list)