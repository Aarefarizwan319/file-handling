
file = open("file.txt", "r")
Counter = 0


Content = file.read()


CoList = Content.split("\n")


for L in CoList:
    if L:
      Counter += 1

print('This is the number of lines:')
print(Counter)

