# functions

# DRY (Do not repeat yourself)

# function
# declaration/definition
# arguments (input to the function)
# return (output of the function)
# body (process performed by the function)

# def <func_name>(<args>?):
#	...
#	body
#	...
#	return?

# function to greet a person
def greet_person(name):
	print(f"Hello, {name}")
	return

# welcome_person = greet_person

# calling a function
# ret = greet_person("John")
# print("return value is ", ret)




def get_greatest_of_three(n1, n2, n3):
	if n1>n2 and n1>n3:
		return n1
	elif n2>n1 and n2>n3:
		return n2
	elif n3>n1 and n3>n2:
		return n3
	elif n1==n2 and n1==n3:
		return n1
	elif n1==n2 and n1>n3:
		return n1
	elif n2==n3 and n2>n1:
		return n2
	elif n1==n3 and n1>n2:
		return n3


# num1 = int(input('Enter first number: '))
# num2 = int(input('Enter second number: '))
# num3 = int(input('Enter third number: '))

# greatest = get_greatest_of_three(num1, num2, num3)
# print("greatest value is ", greatest)


# global variables
# local variables

# global scope
x = 10
y = 20
z = 30

def rand_func():
	global x
	# local scope
	x = x + 20
	print(f"{x=}, ref = {id(x)}")

# print(f"{x=}, ref = {id(x)}")
# rand_func()
# print(f"{x=}, ref = {id(x)}")


# factorial of a number
# 4! = 4 * 3 * 2 * 1

def find_factorial_reverse(num):
	'''
	This function finds the factorial of a number
	by iterating in a reverse order
	'''
	result = 1
	for i in range(num, 0, -1):
		result = result * i
	return result

def find_factorial_forward(num):
	'''
	This function finds the factorial of a number
	by iterating in a forward order

	Arguments:
	* num: int -> number of which factorial is needed to be calculated
	'''
	result = 1
	for i in range(1, num+1):
		result = result * i
	return result


def main():
	num = int(input("Enter a number: "))

	result_1 = find_factorial_forward(num)
	result_2 = find_factorial_forward(num+1)
	result_3 = find_factorial_forward(num+2)
	print(f"results are {result_1}, {result_2}, {result_3}")

	# print(help(find_factorial_forward))
	# s1 = 'hello, world'
	# s2 = "'hello , world'"
	# s3 = """ "hello world" """
	# print(s3)


main()