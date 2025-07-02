new_file=open("newfile.txt","x")
new_file.close()

import os
if os.path.exists("myfile.txt"):
    os.remove("myfile.txt")
else:
    print("file doesn't exist")
myfile=open("myfile.txt","w")
myfile.write(" To split the file into words, we need to use the split() function.")
myfile.close()

os.remove("codingal.txt")
os.rmdir("hello")
