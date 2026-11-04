def countdown(number):
    if number == 0: #? base case
        print("Go!")
    else:
        print(number)
        countdown(number-1) #? Recursive case, Progress (number-1)
countdown(3)

def reduce(number):
    if number == 0:
        print(number)
        return
    else:
        print(number)
        reduce(number-1)
reduce(5)