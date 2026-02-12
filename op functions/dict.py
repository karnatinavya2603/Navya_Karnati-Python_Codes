#Accessing Elements
d = {"name": "Navya", "age": 22}
print(d["name"])      # Navya
print(d.get("age"))   # 22
#Add or Update Elements
d = {"name": "Navya"}
# Add
d["age"] = 22
# Update
d["age"] = 23
print(d)

#Remove Elements

d = {"name": "Navya", "age": 22}
d.pop("age")
print(d)

#popitem
d.popitem()
print(d)

#Dictionary Methods
#keys()
print(d.keys())

#values()
print(d.values())

#items()
print(d.items())

#update()
d1 = {"a": 1}
d2 = {"b": 2}

d1.update(d2)
print(d1)

#clear()
d.clear()

#Example
s = "banana"
freq = {}

for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print(freq)
