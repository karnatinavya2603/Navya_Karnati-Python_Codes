#Set 
s = {1, 2, 3, 3, 4}
print(s)  

#Add Element 
s.add(5)
print(s)  

#Remove Element 
s.remove(2)  
print(s)  

#set operations 
s1 = {1, 2, 3}
s2 = {3, 4, 5}

print(s1.union(s2))        
print(s1.intersection(s2)) 
print(s1.difference(s2)) 
s1.clear()
print(s1)  

#Dictionary 
student = {"name": "Navya", "age": 22}
print(student)

#Access value 
print(student["name"])  

#Add or update
student["course"] = "Python"  
student["age"] = 23           
print(student)


#Remove  the key
del student["age"]
print(student)

student.pop("course")
print(student)

#Boolean 
a = True
b = False
print(a, b)
print(a and b)  
print(a or b)   
print(not a)  

#Example with Numbers
x = 10
y = 5

print(x > y)  
print(x == y) 








