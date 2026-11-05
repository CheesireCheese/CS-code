#ai
def IterativeVowels(value):
    total = 0
    LengthString = len(str(value))  #* string
    for x in range(LengthString):
        FirstCharacter = value[0]
        if FirstCharacter == 'a' or FirstCharacter == 'e' or FirstCharacter == 'i' or FirstCharacter == 'o' or FirstCharacter == 'u':
            total += 1
        value = value[1:len(value)]
    return total

#aii
print(IterativeVowels("house"))

#bi
def RecursiveVowels(value):
    Length = len(str(value))
    total = 0
    if Length == 0:
        return 0
    FirstCharacter = value[0]
    if FirstCharacter == 'a' or FirstCharacter == 'e' or FirstCharacter == 'i' or FirstCharacter == 'o' or FirstCharacter == 'u':
        total += 1
    total = total + RecursiveVowels(value[1:Length])
    return total

#bii
print(RecursiveVowels("imagine"))