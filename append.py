firstfile = input("Enter the name of first file: ")
secondfile = input("Enter the name of second file: ")


f1 = open(firstfile, 'r')
f2 = open(secondfile, 'r')



f1.close()
f2.close()


f1 = open(firstfile, 'a')
f2 = open(secondfile, 'r')


f1.write(f2.read())

f1.close()
f2.close()
