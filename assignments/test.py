value = 4725 #int(input("enter number "))
total = 0
while value != value //10:
    total += (value % 10)
    value = value // 10
print(total)

def sum(number):
    if len(str(number)) == 1:
        return number
    else:
        total = number % 10 + sum(number // 10)
    return total
    

print(sum(4725))