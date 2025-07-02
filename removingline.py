outputFile = open('UpdatedFile.txt', "w")
inputFile = open('Repeated.txt', "r")
lines_seen_so_far = []
print("Eliminating duplicate lines....")
for line in inputFile:
    if line not in lines_seen_so_far:
        outputFile.write(line)
        lines_seen_so_far.append(line)
inputFile.close()
outputFile.close()