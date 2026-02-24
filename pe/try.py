#Zero divivsion error 
try:
    a = int(input("Enter number: "))
    b = int(input("Enter divisor: "))
    print(a / b)
except ZeroDivisionError:
    print("Cannot divide by zero")

#Value Error 

try:
    num = int(input("Enter number: "))
    print(num)
except ValueError:
    print("Invalid Input! Please enter numbers only.")

#File Not Found Error 
try:
    f = open("data.txt", "r")
    print(f.read())
    f.close()
except FileNotFoundError:
    print("File does not exist")

#Multiple Exceptions 
try:
    a = int(input("Enter number: "))
    b = int(input("Enter divisor: "))
    print(a / b)
except ZeroDivisionError:
    print("Division by zero error")
except ValueError:
    print("Invalid input") 
#Using as Keyword 
try:
    f = open("data.txt", "r")
except Exception as e:
    print("Error occurred:", e)

#using else block 
try:
    a = 10
    b = 2
    print(a / b)
except ZeroDivisionError:
    print("Error")
else:
    print("No error occurred") 

#Using Finally block 
try:
    f = open("data.txt", "r")
    print(f.read())
except FileNotFoundError:
    print("File not found")
finally:
    print("Execution completed")

