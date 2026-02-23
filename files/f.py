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

def count_lines(a):
    try:
        f = open(a,"r")
        lines_count = 0 
        for i in f:
            lines_count+=1 
        f.close()
        return lines_count
    except:
        print("File Not error ")
print(count_lines("Solutions.txt"))

def count_words(a):
    f = open(a,"r")
    b = f.read()
    words = b.split()
    count = len(words)
    f.close()
    return count
print(count_words("Solutions.txt")) 
def count_char(a):
    try:
        f = open(a,"r")
        b = f.read()
        c = len(b)
        f.close()
        return c 
    except:
        print("File Not Found Error")
print(count_char("Solutions.txt"))

    
