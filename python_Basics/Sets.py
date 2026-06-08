collection ={5,34,2,3,4}
# print(collection)
# print(type(collection)) 
empty = set()
## Sets are mutable but the elements are immutable 
empty.add(1)
empty.add(2)
empty.add(1)
# empty.remove(3)## if this is not exist in the set so it will give error 
empty.add((1,2,3,4))
## set's does not support lists, and dictionary becuase they are mutable
# empty.clear() ## it makes the set empty 
# print(collection.pop())## it gives the one value at a time in random order 
# print(len(empty))

## Union and intersection in sets of python 
set1 = {1,2,3}
set2 = {3,4,5}

print(set1.union(set2))
print(set1.intersection(set2))
# they both gives the new set does not change the old one
