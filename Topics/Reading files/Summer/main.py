#  write your code here 
file = open("data\\dataset\\input.txt", "r")
counter = 0
for line in file:
    if line == "summer\n":
        counter += 1

print(counter)