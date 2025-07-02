with open('codingal.txt', 'w') as file:
    file.write(" To split the file into words, we need to use the split() function.")
    file.close()

with open('codingal.txt', 'r') as file:
    data = file.readlines()
    print("Words in this file are....")
    for line in data:
        word=line.split()
        print(word)
file.close()