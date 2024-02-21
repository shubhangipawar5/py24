# list is a derived data type and Mutable with mixed data/hetrogeneous
# Direct way of writing list
mylist = [1,2,3,4,5,"shubhh","som","aayu"]
# Accessissng list
print(mylist[2])
print(mylist[5])
# define list with constructor or type casting
str = "shubhangi"
# list()
ml = list(str)
print(ml)   #['s', 'h', 'u', 'b', 'h', 'a', 'n', 'g', 'i']
print(list("aeiou")) #['a', 'e', 'i', 'o', 'u']

# Change List Items
# Python lists are mutable. Meaning lists are changeable.

languages = ['Python', 'Swift', 'C++']

# changing the third item to 'C'
languages[2] = 'C'
print(languages)  # ['Python', 'Swift', 'C']


mylist = [1,2,3,4,5,"shubhh","som","aayu"]
# Negative Indexing
print(mylist[-1])  #aayu

print(mylist[-3]) #shubhh

# Slicing list
print(mylist[0:-1])  #upto -1 index from start
print(mylist[-3:])  #upto -3 index to last ['shubhh', 'som', 'aayu']
print(mylist[:])
print(mylist[2:])
print(mylist[::-1])    #Reverses a list with step/jump value -1 ['aayu', 'som', 'shubhh', 5, 4, 3, 2, 1]
print(mylist[-1:-2])  #returns empty list[] ,bcs end point is less than start point

# slicing with step/jump value
# listName[startindex:stopindex:stepvalue)
print(mylist[::1])  #slice with jump 1- [1, 2, 3, 4, 5, 'shubhh', 'som', 'aayu']
print(mylist[::2])  #slice with jump 2- [1, 3, 5, 'som']

# Access Nested List
nestList = [1, 2, 3, 4, 5, 'shubhh', 'som', 'aayu',["a","b","c"]]
print(nestList[5])  #shubhh
print(nestList[8][1])  #b
nestList2 = [1, 2, 3, 4, 5, 'shubhh', 'som', 'aayu',["a","b","c",[11,12,13,14,15]]]
print(nestList2[8][3][2])    #13


# LIST METHODS

# Edit the list
list1 = [1,2,3,4,5]
# 1.insert   --inserts element at given specific index
print(list1.insert(2,"A"))
print(list1)   #[1, 2, 'A', 3, 4, 5]

# 2. The append() method adds an item at the end of the list.
list2 = [1,2,"shub"]
print(list2.append("aayu"))
print(list2)  #[1, 2, 'shub', 'aayu']

# 3. Extend a-dd all/many  items of an iterable(str,tupple,dict,list) to the end of the list

l1 = [1,2,3,4]
l2 = ["a","b","c","d"]
print(l1.extend(l2))
print(l1)   #[1, 2, 3, 4, 'a', 'b', 'c', 'd']

# 4. Remove/ delete element of an list
# remove - removes the given item
l3= [1,2,3,4,5,6,7,"shubh"]
print(l3.remove("shubh"))
print(l3)  #[1, 2, 3, 4, 5, 6, 7]

# we can also use del statement in py- works for given index
del l3[1]
print(l3)  #[1, 3, 4, 5, 6, 7]  - first index element is deleted
del l3  # l3 itself deleted and returns error name 'l3' is not defined.
# print(l3)

# 5. POP -pop() function can also be used to remove and return an element from the list, but by default it removes only the last element of the list,
l4 = ['a','b','c','d']
print(l4.pop(2))
print(l4) #  remove index 2 element
print(l4.pop()) # by default last element removes nad returns that removed element -"d"
print('a' and 'b' in l4)    #true

# 6. clear - clears all list
l5 = [1,2,3,4,5]
print(l5.clear())
print(l5)  #returns empty list


# 7. length
print(len(l4))


# 8. reverse
l7=[1,2,3,4,5,6]
print(l7.reverse())
print(l7)

# 9. sort
l6 = [5,4,7,1,2,3]
l6.sort()
print(l6)  #[1, 2, 3, 4, 5, 7]

# 10 Index- returns the index of the first matched item
l8= ['a',"shubh","aayu"]
print(l8.index("aayu"))  #2

#  11. Count- Return number of occurrences of value

l9= ['a',"shubh","aayu",'a',1,3,'a']
print(l9.count('a'))  #3
print('********ITERATING list************')
# ITERATING list
languages = ['Python', 'Swift', 'C++']
for item in languages:
    print(item)




# concatenation of two lists
# declaring the lists
list1 = [12, 14, 16, 18, 20]
list2 = [9, 10, 32, 54, 86]
# concatenation operator +
l = list1 + list2

print(l)



""" append(),insert(),extend(),remove(),pop(),pop(index),
copy(),list(),sort(),sort=(reverse=true),index(),count()
"""

