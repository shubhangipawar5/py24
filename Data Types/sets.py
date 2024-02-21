# Sets are unique,No indexed, immutable,unordered,hetrogeneous
vowel_letters = {'a', 'e', 'i', 'o', 'u'}
print(vowel_letters)
mixed_set = {'Hello', 101, -2, 'Bye'}
print('Set of mixed data types:', mixed_set)

"""
Method: 	Description
add()	Adds an element to the set
clear()	Removes all elements from the set
copy()	Returns a copy of the set
difference()	Returns the difference of two or more sets as a new set
difference_update()	Removes all elements of another set from this set
discard()	Removes an element from the set if it is a member. (Do nothing if the element is not in set)
intersection()	Returns the intersection of two sets as a new set
intersection_update()	Updates the set with the intersection of itself and another
isdisjoint()	Returns True if two sets have a null intersection
issubset()	Returns True if another set contains this set
issuperset()	Returns True if this set contains another set
pop()	Removes and returns an arbitrary set element. Raises KeyError if the set is empty
remove()	Removes an element from the set. If the element is not a member, raises a KeyError
symmetric_difference()	Returns the symmetric difference of two sets as a new set
symmetric_difference_update()	Updates a set with the symmetric difference of itself and another
union()	Returns the union of sets in a new set
update()	Updates the set with the union of itself and others
"""


print("**********************")

# Retreive by loop only

for i in mixed_set:
    print(i)

print("**********************")

# add()   // add single element
mixed_set.add("Aayush")
print(mixed_set)

# add many element with update()
lst = [11,12,13,14]
mixed_set.update(lst)
print(mixed_set)
mixed_set.update({'a','b','c'})
mixed_set.update([1,2,3,4])

# remove() -> remove with given value
mixed_set.remove(11)
print(mixed_set)


# Discard()  -> discards element even it is present in the set or not present and returns None.
mixed_set.discard("Aayush")
print(mixed_set)

# POP()   -> pop out any random element
vowel_letters.pop()
print(vowel_letters)


# clear() -> clears data in the set-> returns empty set()

vowel_letters.clear()
print(vowel_letters)


# del()  -> deletes the data type from memory
del vowel_letters
# print(vowel_letters)   #name 'vowel_letters' is not defined


print("**********************")

# Union() -> The union of two sets A and B include all the elements of set A and B.
A={1,2,3,4,'a'}
B={'a','b','c',1,2}

print(A | B)    #{1, 2, 3, 4, 'b', 'c', 'a'}
print(A.union(B))      #{1, 2, 3, 4, 'b', 'c', 'a'}


# Intersect -> The intersection of two sets A and B include the common elements between set A and B.

print(A&B)    #{1, 2, 'a'}   #common elements
print(A.intersection(B))    #{1, 2, 'a'} #common elements

# SUBSET & SUPERSET

setA = {1,2,3,4,5}
setB = {1,2}

print(setB.issubset(setA))   #True if all elements of setB is present in setA
print(setA.issuperset(setB))   #True if all elements of setB is present in setA


# check 2 sets are equal
# We can use the == operator to check whether two sets are equal or not

print(setA == setB)   #returns b oolean

# difference - > setA  and setB  gives difference values
print(setA - setB)   #{3, 4, 5}
print(setA.difference(setB))  #{3, 4, 5}
print(setB.difference(setA))  # if No difference then -> empty set()


"""
Set Symmetric Difference
The symmetric difference between two sets A and B includes all elements of A and B without the common elements.
"""

# opposit to intersectio-> all elements other than common in 2 sets
s1 = {1,2,3,4,5}
s2 = {2,3,4,8,9,7}

print(s1.symmetric_difference(s2))   #{1, 5, 7, 8, 9}


# difference()
setA = {11,22,33}
setB = {11,22,44}
print(setA.difference(setB))    #33
print(setB.difference(setA))    #44

# differenceUpdate()
setC = {11,22,33}
setD = {11,22,44}

#print(setC.difference(setD))
setC.difference_update(setD)
print(setC)