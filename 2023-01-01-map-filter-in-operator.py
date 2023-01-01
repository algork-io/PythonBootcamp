# in operator

def check_item_in_iterable(item, iterable):
	'''
	Checks if item exists in iterable
	'''
	exists = item in iterable
	return exists

s1 = "Hello World"
s2 = "World"

l1 = ['apple', 'orange']
item = 'Apple'

# check_item_in_iterable(s2, s1)
# check_item_in_iterable(item, l1)


# nested_list = [ [1,2], [3,4], [5,6], [[1,2], [3,4]] ]
# for item in nested_list:
# 	for subitem in item:
# 		print(subitem, end=" ")
# print()

# if check_item_in_iterable("hello", "Hello world"):
# 	print("yes")
# else:
# 	print("no")	


# map, filter

# lambda function

# check_item_in_iterable_lambda = lambda i, j: i in j

# map function

# converts items in an iterable

# [1,2,3,4,5]
# [2,4,6,8,10]

l1 = [1,2,3,4,5]
l2 = []
# for i in l1:
# 	l2.append(i*2)
# print(l1, l2)

def mult_by_2(num):
	return num * 2

# modified_list = list(map(mult_by_2, l1))
# modified_list = list(map(lambda num: num*2, l1))

# print(modified_list)





# result = list(map(int, input("enter the numbers: ").split(',')))
# print(result)

# generate random emails

# def generate_emails(names):
# 	'''
# 	returns a random email for n number of users
# 	'''
# 	usernames = list(map(lambda name: name.strip().replace(" ", ".")  , names))
# 	emails = list(map(lambda username: username + '@gmail.com', usernames))
# 	return emails


def generate_emails(names):
	'''
	returns a random email for n number of users
	'''
	return list(map(lambda name: name.strip().replace(" ", ".") + '@gmail.com'  , names))


# names = input("Enter names: ").split(",")
# emails_list = generate_emails(names)
# upper_case_names = list(map(lambda x: x.upper(), names))
# print(emails_list)
# print(upper_case_names)



# filter
# remove elements in list which dont satisfy a condition
nums = [1,2,3,4,5,6]

print(list(filter(lambda x: not bool(x%2), nums)))


# exercise

'''
1. function takes a list and returns mean/avg, mode, median, std devian, smallest, largest
2. function to shift the numbers (list, shift)
	[1,2,3,4,5]
	output: [5,1,2,3,4] (1)
	output: [4,5,1,2,3] (2)
3. Reverse a list (2 methods, using slicing, using loops, use shifting function)
4. Read a list of numbers 'L' from user and another number 'n'
	find all elements smaller than 'n' in 'L'

5. function to remove duplicates from an array/list
6. function to remove unique values from array/list
7. Take 2 input matrices from user and multiply (2D lists)
	
'''


