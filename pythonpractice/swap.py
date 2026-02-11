#Using temp 
a = int(input("Enter num1:"))
b = int(input("Enter num2:"))
temp = a 
a = b 
b = temp
print("a=",a)
print("b=",b)

#without temp 
a = int(input("Enter num1:"))
b = int(input("Enter num2:"))
a,b = b,a 
print("a=",a)
print("b=",b)

#with Arthematic 
a = int(input("Enter num1:"))
b = int(input("Enter num2:"))
a = a+b 
b = a-b 
a = a-b 
print("a=",a)
print("b=",b)

#with XOR 
a = int(input("Enter num1:"))
b = int(input("Enter num2:"))
a = a^b 
b = a^b 
a = a^b
print("a=",a)
print("b=",b)