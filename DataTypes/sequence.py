#List 
numbers = [10,20,30,40]
print(numbers)

#Acess List Elements 
numbers = [10,20,30,40]
print(numbers[0])
print(numbers[3])

#Append Element 
numbers = [10,20,30,40]
numbers.append(50)
print(numbers)

#Update Element 
numbers = [10,20,30,40]
numbers[1] = 25 
print(numbers)

#Remove Element 
numbers = [10,20,30,40]
numbers.remove(30)
print(numbers) 

#Length of the list 
numbers = [10,20,30,40]
print(len(numbers))

#Adding the Elements 
numbers = [10,20,30,40]
print(sum(numbers))

#Tuple Coding Questions 
#Create a Tuple 
colors = ("Red","Blue","Yellow","orange")
print(colors)
#Acess Tuple Elements 
colors = ("Red","Blue","Yellow","orange")
print(colors[0])
#Tuple Slicing 
print(colors[0:2])
#Count Element in tuple 
t = (1, 2, 2, 3, 2)
print(t.count(2))
#Index in tuple 
print(t.index(3))
#Convert tuple to list 
lst = list(t)
print(lst)

