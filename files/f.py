#file handling 
f = open("Solutions.txt","r")
str = f.read()
print(str)
f.close() 

f = open("Solutions.txt","r")
str = f.readline()
print(str)
f.close() 

f = open("Solutions.txt","r")
str = f.readlines()
print(str)
f.close()

def file_read(a):
    file =open(a,"r")
    data = file.read()
    file.close()
    return data
print(file_read("Solutions.txt"))

def file_read(a):
    file =open(a,"r")
    data = file.readline()
    file.close()
    return data
print(file_read("Solutions.txt"))

def file_read(a):
    file =open(a,"r")
    data = file.readlines()
    file.close()
    return data
print(file_read("Solutions.txt"))

def file_read(a):
    file = open(a,"r")
    data = file.read()
    for i in data:
        print(i)
    return i
print(file_read("Solutions.txt"))

    
