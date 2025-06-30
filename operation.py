file = open("file.txt","r")
print(file.read(11))
file.close()

file = open('file.txt', 'r')
print("Reading first line of file")
print(file.readline())
file.close()

file = open('file.txt', 'r')
print("Reading multiple lines...")
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

file = open('file.txt','r')
print("Looping through lines")
for loop in file:
    print(loop)
file.close()

