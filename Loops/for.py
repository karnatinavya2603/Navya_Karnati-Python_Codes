


for i in range(1,100):
    print(i)

n = 50
for i in range(1,n+1):
    if i%2==0:
        print("Even")
   

n= 50 
for i in range(1,n+1):
    if i%2!=0:
        print("odd")

n = 6
for i in range(1,11):
    print(f"{n}*{i} = {n*i}") 

n = 5 
sum =0 
for  i in range(n):
    sum = sum+i 
print(sum)

n = 4 
fact = 1 
for i in range(1,n+1):
    fact = fact*i 
print(fact)

n = 123
rev = 0
while n>0:
    rev = rev*10+n%10 
    n = n//10 
print(n)

a = 123 
count = 0 
while a >0:
    a = a//10 
    count+=1
print(count)

a =101
rev = 0
while a >0:
    rev = rev*10+rev/10 
    a=a//10
if a ==rev:
    print("Palindrome")
else:
    print("Not a palindrome")


    

