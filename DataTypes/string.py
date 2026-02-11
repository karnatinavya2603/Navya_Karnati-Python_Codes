#Create String 
s1 = 'Hello'
s2 = "Python"
print(s1)
print(s2)

#Acess Characters 
s = "Python"
print(s[0])   
print(s[-1]) 

#string slicing
s = "Python"
print(s[0:4])  
print(s[2:])   
print(s[:3])   
print(s[::-1])

#string Length 
s = "Python"
print(len(s)) 

#string Concatenation 
s1 = "Hello"
s2 = "World"
s3 = s1 + " " + s2
print(s3)  

#string repetation 
s = "Hi! "
print(s * 3)  

#check substring 
s = "Python"
print("tho" in s)   
print("java" not in s)  

#convert case 
s = "python"
print(s.upper())  
print(s.lower())  
print(s.title())  

#Remove spaces 
s = "   Hello Python   "
print(s.strip())  

#split and Join 
s = "Python is fun"
words = s.split()
print(words)  # ['Python', 'is', 'fun']

joined = "-".join(words)
print(joined)  # Python-is-fun

#Replace string 
s = "I like Java"
s = s.replace("Java", "Python")
print(s)  







