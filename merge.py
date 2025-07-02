file1 = open('file3.txt', 'r')
file2 = open('openfile_doc.txt', 'r')
data1 = file1.read()
data2 = file2.read()
if data1 == data2:
    print("Files are same")
else:
    print("Files are different")
file1.close()
file2.close()
with open('MergedFile.txt', 'w') as fp:
    fp.write(data1 + data2)