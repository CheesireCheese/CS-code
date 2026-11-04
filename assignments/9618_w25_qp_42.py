#2a
import random
array = random.sample(range(0,101),20)
#2b
def PrintArray(array):
    for i in range(len(array)):
        print(array[i], end=" ")

#2c
def BubbleSort(array):
    max = len(array)
    for i in range(max):
        swapped = False
        for j in range(max-1):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1], array[j]
                swapped = True
        if not swapped:
            break
    max = max -1
    
    return array

#di
