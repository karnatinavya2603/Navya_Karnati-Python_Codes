s = {1, 2, 3}
s.add(4)
print(s)
#update
s = {1, 2}
s.update([3, 4])
print(s)
#remove 
s = {1, 2, 3}
s.remove(2)
print(s)

#discard
s = {1, 2, 3}
s.discard(2)   # No error
print(s)
#pop 
s = {10, 20, 30}
s.pop()
print(s)

#clear
s = {1, 2, 3}
s.clear()
print(s)

#union 
a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))

#intersection
print(a.intersection(b))

#difference
print(a.difference(b))
#check subset
a = {1, 2}
b = {1, 2, 3, 4}
print(a.issubset(b))

#unique elements
nums = [1, 2, 2, 3, 4, 4, 5]
unique = set(nums)
print(unique)



