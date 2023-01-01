# conditional statements

# elif
#  if statement


# if user enters 1 print 'One' or if user enters 2 print 'two' if user enters anything else print not found


# num = int(input('enter a number'))

# if num == 1:
# 	print('One')

# elif num == 2:
# 	print('Two')

# else:
# 	print('Not found')

# if False:
# 	print('true')


# check if a number is odd or even

# num = int(input('Enter a number'))

# result = num%2

# if result == 0:
# 	print('number is even')
# else:
# 	print('number is odd')



# check if user input is a vowel or not


# user_input = input('Enter a char')

# if user_input == 'a':
# 	print('char is a vowel')

# elif user_input == 'e':
# 	print('char is a vowel')

# elif user_input == 'i':
# 	print('char is a vowel')

# elif user_input == 'o':
# 	print('char is a vowel')

# elif user_input == 'u':
# 	print('char is a vowel')

# else:
# 	print('char not found')



# nesting (if else)

# w.a.p to display 'Grade 1' if a number is divisible by 2 and is <= 10, 
# 'Grade 2'  if a number is divisible by 3 and > 10

# To be submitted.......

# num = int(input('enter a number')) #12

# result_2 = num%2 #0
# result_3 = num%3 #0


# if result_2 == 0:
# 	if num <= 10:
# 		print('Grade 1')

# elif result_3 == 0:
# 	if num > 10:
# 		print('Grade 2')



# display the last digit of a number

# num = int(input('Enter a number'))

# last_digit = num%10

# print('last digit is ',last_digit)


# Logical gates
# And, or, not


# and => (condition is true when both conditions around and are true)
# or -> ()
# not => 



# w.a.p to display 'Grade 1' if a number is divisible by 2 and is <= 10, 
# 'Grade 2'  if a number is divisible by 3 and > 10



num = int(input('enter a number')) #12

if num%3 == 0 and num%2 == 0:
	print('divisible by both')

elif num%2 == 0 and num <= 10: 
	print('grade 1')

elif num%3 == 0 and num >10:
	print('grade 2')


#1. w.a.p to check the greatest of 3 numbers (nested if else, logical gates)
#2. w.a.p where user enter a number and print the month according to the number if 0 or greater than 12 print 'this month doesnt exist on earth'
#3. Given an integer, perform the following conditional actions:
	# 	If n is odd, print Weird
	# 	If n is even and in the inclusive range of 2 to 5, print Not Weird			
	# 	If n is even and in the inclusive range of 6 to 20, print Weird
	# 	If n is even and greater than 20, print Not Weird








