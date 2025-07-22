# set is a collection of unique elements
#set is unordered element and must be unique
odds = set([1,3,5,7,9,2])
evens = set([2,4,6,8,10])

#union is a collection of 2 sets all together
print(odds.union(evens))
print(evens.union(odds))

#intersection is only same element that inside 2 sets
print(odds.intersection(evens))

#add element
#call example is a set
example = set()
example.add(42)
example.add(False)
print(len(example))
print(example)

#clear a set
example.clear()
print(len(example))

example2 = set(["H", "E"])
print(example2)
example2.remove("H")
print(len(example2))

#test if element inside set collection
example3 = set([1,"Ok"])
print(1 in example3)
print("Yes" in example3)