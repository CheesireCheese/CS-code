my_list = [11, 12, 22, 25, 34, 64, 90]
target_value = 64
found = False

low, high = 0, len(my_list) - 1             #? set low and high var

while low <= high:
    mid = (low + high) // 2                 #? get value for half
    if my_list[mid] == target_value:        #? find value
        found = True
        break
    elif my_list[mid] < target_value:
        low = mid + 1                       #? low on the left = the low on the right
    else:
        high = mid - 1                      #? high on the right = the high on the left

if found:
    print("Value found at index", mid)
else:
    print("Value not found")