with open("score.txt") as file:
    data = file.read()
print(data)

for line in file:
    print(line)

Line = "Ali"
print(repr(line)) 			#‘Ali\n’
print(repr(line.strip()))	#‘Ali’
record = "Ali,72"
Parts = record.split(",")

try:
    with open("Scores.txt","r") as file:
        data = file.read()


        print(data)


except FileNotFoundError:
    print("Scores.txt could not be found")