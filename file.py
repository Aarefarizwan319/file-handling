with open("file.txt", "r") as file:
    content = file.read()
    print("Full content of the file:")
    print(content)

with open("file.txt", "r") as file:
    first_10_chars = file.read(10)
    print("\nFirst 10 characters of the file:")
    print(first_10_chars)

with open("file.txt", "r") as file:
    first_line = file.readline()
    print("\nFirst line of the file:")
    print(first_line.strip())

with open("file.txt", "r") as file:
    print("\nFirst four lines of the file:")
    for i in range(4):
        line = file.readline()
        if not line:
            break
        print(line.strip())

with open("file.txt", "r") as file:
    print("\nAll lines in the file:")
    for line in file:
        print(line.strip())
