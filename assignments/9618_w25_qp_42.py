#2a
import random
array = random.sample(range(0,101),20)  #1d array of integer
#2b
def PrintArray(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()
#2c
def BubbleSort(array):
    max = len(array)    #integer
    for i in range(max):
        swapped = False #boolean
        for j in range(max-1):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1], array[j]
                swapped = True
        if not swapped:
            break
    max = max -1
    
    return array

#di
PrintArray(array)
print("Sorted")
sortedarray = BubbleSort(array) #1d array of integer
PrintArray(sortedarray)

#e
def RecursiveBinarySearch(intarray, lower, upper, value):
    mid = (upper + lower) // 2 #integer
    if lower <= upper:
        if value == intarray[mid]:
            return "value at intex", mid
        elif value > intarray[mid]:
            return RecursiveBinarySearch(intarray, mid + 1, upper, value)
        else:
            return RecursiveBinarySearch(intarray, lower, mid - 1, value)
    else:
        return "Not found"

#fi
Integer = int(input("enter value "))
print(RecursiveBinarySearch(array, 0, 19, Integer))