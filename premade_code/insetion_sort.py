my_list = [3,5,2,8,9,1]

for i in range(1, len(my_list)):        #? i represents the index of the current element being compared
    key = my_list[i]
    j = i - 1                           #? j will continue to decrease until the key > than the previouse element
    while j >= 0 and key < my_list[j]:  #? shift the previous element to the right to make space for the key
        my_list[j + 1] = my_list[j]     #? move the previous element to the right
        j -= 1
    my_list[j + 1] = key

print("Sorted list is:", my_list)