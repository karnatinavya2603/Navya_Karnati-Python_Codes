
#Append
numbers = [10, 20, 30, 40]
numbers.append(50)
print(numbers)

#Extend 
numbers = [10,20,30,40]
numbers.extend([50,60]) 
print(numbers) 

#Insert 
numbers = [10,20,30,40]
numbers.insert(1,50)
print(numbers)

#Remove 
numbers = [10,20,30,40]
numbers.remove(40)
print(numbers) 

#pop 
numbers = [10,20,30,40,50]
numbers.pop()
numbers.pop(1)
print(numbers)

#clear 
numbers.clear()
print(numbers)

#index
numbers = [10,20,30]  
numbers.index(20)
print(numbers)

#count 
numbers.count(20)
print(numbers)

#sort 
numbers.sort()
print(numbers)

#Length
numbers = [10,20,30,40]
len(numbers)
