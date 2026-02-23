file.txt='''Hi My name is Navya"
"Welcomw to python'''
def read_file(a):
    data = open(a,"r")
    b = data.read()
    data.close()
    return b
print(read_file("file.txt")) 
    
