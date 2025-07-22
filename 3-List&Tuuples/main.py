
# list can store different types of elements..kind of array

age = [10, 12, 13, 23, 18]  # index 0,1,.....
print(age)  # all value
print(age[0])  # 10
print(type(age))  # <class 'list'>
print(len(age))  # length
age[0] = 234  # possible but not possible in str
print(age)
# same rule for slicing [check str file]
# check for float,str,bool

# we can store int,float,str in one list
hudai = [1, 2.3, "Farhad"]
print(hudai)

# Methods of list
list = [1, 5, 3]
list.append(4)  # add 4 at the end 1 5 3 4
list.sort()  # sort in ascending
list.sort(reverse=True)  # sort in descending
list.reverse()  # reverse the list

list.insert(1, 100)  # at index 1 add 100
print(list)
list.remove(100)  # remove first 100
print(list)
list.pop(2)
print(list)  # remove 2 index
#  check with list.


# Tuples
# we cannot change value ===  immutable just like str
a = (1, 2, 3, 4)
# a[0] = 100 Erooooor
# for single value tuple
b = (1,)  # without , it is int
c = (1)
print(type(c))  # int
print(type*b)  # tuple

# also slicing work (same rule as str)

# Method

print(a.index(1))  # return the index of val
print(a.count(1))  # return count of val
