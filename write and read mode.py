file_read = open("file.txt", "r")
print("File in Read Mode :-")
print(file_read.read())
file_read.close()


file_write = open("file.txt", "w")
file_write.write("File in write mode ...\n")
file_write.write("Hi! I am Penguin. I am 1 yr. old")
file_write.close()


file_append = open("file.txt", "a")
file_append.write("\nFile in append mode ...\n")
file_append.write("Hi! I am Penguin. I am 1 yr. old")
file_append.close()
