# simple data types
# int, str, bool, float, None

# Complex data types
# List (Array in C, etc)
# Tuple (like array)
# Dict (Object in JS, Map in some other languages)

# iterable
# some data that can be iterated/looped over

# List
# my_fav_numbers = [1, 2, 3, 4, 5]
# empty_list = []
# print(len(my_fav_numbers))
# print(empty_list)

# string is also an iterable
# a = 'hello world'
# print(len(a))


# C code
# int arr[] = [1,2, 'arr']

# can store heterogenous data types in list unlike C/other languages
my_list = ['Apple', 'Cherry', True, 1.4, 2, None]

# print(my_list)


# for i in [1,2,3,4,5,6,7,8,9,10]:
# 	print(i)
# print("loop end")
# for i in my_list:
# 	print(i)

# Indexing
# access first element in list
# print(my_list[0])

# reverse indexing
# print(my_list[-2])


# my_str = "Hello, World!"

# print(my_str[-1])
# for i in my_str:
# 	print(i, end="")


# Slicing 
# my_list = [1,2,3,4,5,6]

# my_list_small = my_list[0:3]
# my_list_skipped = my_list[0::2]


# my_list_rev = my_list[-1::-1]

# my_list_rev_2 = my_list[::-1]

# print(my_list_rev_2)

# a = 1
# b = a

# b += 4

# print(a,b)


# every method is a function (append)
# not every function is a method (print is not a method)
# append method on list
# my_list_1 = [1,2,3]
# my_list_1.append(4)
# my_list_1.append(5)

# print(my_list_1)

# list_1 = [1,2,3]
# # copying a list
# list_2_copy = list_1.copy()
# list_2_copy_2 = list_1[:]
# list_2_copy.append(4)
# list_2_copy_2.append(4)

# print(list_1, list_2_copy, list_2_copy_2)

# numbers = input("Please enter some numbers: ")
# total = 0
# for i in numbers:
# 	total += int(i)
# print(total)

# 12,34
# numbers = input("Please enter some numbers: ")
# total = 0
# num = ''
# for i in numbers:
# 	if i == ',':
# 		total += int(num)
# 		num = ''
# 		continue
# 	num += i
# total += int(num)
	# total += int(i)
	# print(f"total is {total}")
# print(total) 

# methods on string
# split
numbers = input("Please enter some numbers: ")
split_nums = numbers.split(",")

split_ints = []
for i in split_nums:
	split_ints.append(int(i))

print(split_ints)
print(sum(split_ints))







>>>
>>> s = "hello, world"
>>> s.capitalize()
'Hello, world'
>>> s
'hello, world'
>>> s += "!"
>>> s
'hello, world!'
>>>
>>> l = [1,2,3,4]
>>> l[0]
1
>>> l[0] = 0
>>> l
[0, 2, 3, 4]
>>>
>>> s
'hello, world!'
>>> s[0]
'h'
>>> s[0] = 'H'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>>
>>> s
'hello, world!'
>>> s = s.capitalize()
>>> s
'Hello, world!'
>>> s = 'hello'
>>> c = s.capitalize()
>>> c
'Hello'
>>> s
'hello'
>>> s.
s.capitalize(    s.isalpha(       s.ljust(         s.split(
s.casefold(      s.isascii(       s.lower(         s.splitlines(
s.center(        s.isdecimal(     s.lstrip(        s.startswith(
s.count(         s.isdigit(       s.maketrans(     s.strip(
s.encode(        s.isidentifier(  s.partition(     s.swapcase(
s.endswith(      s.islower(       s.replace(       s.title(
s.expandtabs(    s.isnumeric(     s.rfind(         s.translate(
s.find(          s.isprintable(   s.rindex(        s.upper(
s.format(        s.isspace(       s.rjust(         s.zfill(
s.format_map(    s.istitle(       s.rpartition(
s.index(         s.isupper(       s.rsplit(
s.isalnum(       s.join(          s.rstrip(
>>> s.casefold()
'hello'
>>> help(s.casefold)

>>> s = '    hello '
>>> s.center()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: center expected at least 1 argument, got 0
>>> help(s.center)

>>>
>>> s = 'hello'
>>> s.center(10)
'  hello   '
>>> s.center(10, '*')
'**hello***'
>>> s.center(11, '*')
'***hello***'
>>>
>>> s.
s.capitalize(    s.isalpha(       s.ljust(         s.split(
s.casefold(      s.isascii(       s.lower(         s.splitlines(
s.center(        s.isdecimal(     s.lstrip(        s.startswith(
s.count(         s.isdigit(       s.maketrans(     s.strip(
s.encode(        s.isidentifier(  s.partition(     s.swapcase(
s.endswith(      s.islower(       s.replace(       s.title(
s.expandtabs(    s.isnumeric(     s.rfind(         s.translate(
s.find(          s.isprintable(   s.rindex(        s.upper(
s.format(        s.isspace(       s.rjust(         s.zfill(
s.format_map(    s.istitle(       s.rpartition(
s.index(         s.isupper(       s.rsplit(
s.isalnum(       s.join(          s.rstrip(
>>> help(s.index)

>>> s
'hello'
>>> s.index('he')
0
>>> s.index('lo')
3
>>> s[3]
'l'
>>> s = 'hello and trello'
>>> s.index('ello')
1
>>> s.index('ello', 4)
12
>>> s[12:]
'ello'
>>> s[11:]
'rello'
>>>
>>> s.
s.capitalize(    s.isalpha(       s.ljust(         s.split(
s.casefold(      s.isascii(       s.lower(         s.splitlines(
s.center(        s.isdecimal(     s.lstrip(        s.startswith(
s.count(         s.isdigit(       s.maketrans(     s.strip(
s.encode(        s.isidentifier(  s.partition(     s.swapcase(
s.endswith(      s.islower(       s.replace(       s.title(
s.expandtabs(    s.isnumeric(     s.rfind(         s.translate(
s.find(          s.isprintable(   s.rindex(        s.upper(
s.format(        s.isspace(       s.rjust(         s.zfill(
s.format_map(    s.istitle(       s.rpartition(
s.index(         s.isupper(       s.rsplit(
s.isalnum(       s.join(          s.rstrip(
>>> s = '123abc'
>>> s.isalnum()
True
>>> s.isalpha()
False
>>> s = '   hello '
>>> s.strip()
'hello'
>>> s.startswith('he')
False
>>> s.startswith('12')
False
>>> s
'   hello '
>>> s = 'alpha'
>>> s.startswith('al')
True
>>> if s.startswith('alp'):
...     print("hello")
...
hello
>>> s.
s.capitalize(    s.isalpha(       s.ljust(         s.split(
s.casefold(      s.isascii(       s.lower(         s.splitlines(
s.center(        s.isdecimal(     s.lstrip(        s.startswith(
s.count(         s.isdigit(       s.maketrans(     s.strip(
s.encode(        s.isidentifier(  s.partition(     s.swapcase(
s.endswith(      s.islower(       s.replace(       s.title(
s.expandtabs(    s.isnumeric(     s.rfind(         s.translate(
s.find(          s.isprintable(   s.rindex(        s.upper(
s.format(        s.isspace(       s.rjust(         s.zfill(
s.format_map(    s.istitle(       s.rpartition(
s.index(         s.isupper(       s.rsplit(
s.isalnum(       s.join(          s.rstrip(
>>> s.upper()
'ALPHA'
>>> s
'alpha'
>>> x = s.upper()
>>> x
'ALPHA'
>>> x.lower()
'alpha'
>>> s = 'Hello'
>>> s.swapcase()
'hELLO'
>>> l = [1,2,3,4]
>>> l.
l.append(   l.copy(     l.extend(   l.insert(   l.remove(   l.sort(
l.clear(    l.count(    l.index(    l.pop(      l.reverse(
>>> l1 = [1,2,3,4]
>>> l2 = [5,6,7,8]
>>> l1.extend(l2)
>>> l1
[1, 2, 3, 4, 5, 6, 7, 8]
>>> l2
[5, 6, 7, 8]
>>> help(l.insert)

>>> l
[1, 2, 3, 4]
>>> l.insert(1, 24)
>>> l
[1, 24, 2, 3, 4]
>>>