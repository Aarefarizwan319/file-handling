file1 = open('file.txt', 'r')
file2 = open('fileUpdated.txt', 'w')
for line in file1:
    if not (line.startswith('Coding')):
        print(line)
        file2.write(line)
file2.close()
file1.close()