filename = input("Enter file name:")
a=''
try:
    f = open(filename)
    f.close()
    a='exists'
except IOError:
    print()

if a=='exists':
    print('File is there')
    n = int(input("1. Press 1 to read containts of:\n "
            "2. Press 2 to delete the file content and start over:\n "
            "3. Append the content to file:"))
    if n==1:
        print("Reading file")
        file1 = open(filename, "r")
        contents = file1.read()
        print(contents)
    elif n==2:
        content = input("Overwriting file, Enter new contents:")
        file2 = open('test.py', 'w')
        file2.write(content)
    elif n==3:
        print("Append the content to file")
        content1 = input("Enter content to add:")
        file3 = open(filename, 'a+')
        file3.write(content1)
        file3.close() 


else:
    print("File doesn't exists")
    data = input("Enter contents for new file:")
    f= open(filename,"w+")
    f.write(data)
    f.close()


    