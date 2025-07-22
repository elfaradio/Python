
# Format
s = "hellO"
s1 = 'kire bhai\nki obostha'  # here \n create new line
s2 = """bhaiiiii"""
s3 = "bhai 'tui vala na' ahare"
print(s1)

# function

x = "a"+"b"  # concatation
print(x)
print(len(x))  # 2
x = "a b"
print(len(x))  # 3
print(x.endswith("b"))  # return True if b diye end hoi
print(x.capitalize())  # a become capital and not original string modified
print(x.replace("a", "c"))  # a replaced by c and not original str modofied
print(x.find('a'))  # first index of a
print(x.count("a"))  # count a
# try to check all str function with s.

# Indexing
ss = "Farhad"
print(ss[0])
# print(ss[10]) IndexError: string index out of range
# ss[0] = 'R' TypeError: 'str' object does not support item assignment


# Slicing

sa = "Farhad"  # also -6 -5 -4 -3 -3 -1 print(sa[-1])->>d
print(sa[1:3])  # 1 theke 2 index
print(sa[:3])  # 0 to 2 index
print(sa[0:])  # o to last index
print(sa[-1])  # d


# Condition

age = 9

if (age >= 18):
    print("Bhai tui adult, kichu rojgar kor jodina rich kid hos")
elif (age > 10):
    print("Porashuna kor")
else:
    print("Tui Baccha")
