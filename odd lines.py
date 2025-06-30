fn1 = open('file.txt', 'r')
fn2 = open('fileUpdated.txt', 'w')

content = fn1.readlines()
type(content)
for i in range(1,len(content)+1):
    if i % 2 != 0:
        fn2.write(content[i-1])

fn2 = open("fileUpdated.txt","r")
print(fn2.read())
fn2.close()
fn1.close()
