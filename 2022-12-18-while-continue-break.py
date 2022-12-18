# while loops
# while condition:
# 	body



# valid input is between 5 and 10

# num = int(input("Please enter a number: "))
# while num < 5 or num > 10:
# 	print("Incorrect value entered, please enter a correct number!\n")
# 	num = int(input("Please enter a number again: "))

# # code execution reaches here when the while condition is false
# print("Entered number is correct and equals ", num)


# break	
# printing tables from 2 to 6 

# counter_1 = 2 # 3
# counter_2 = 1 # 2, 3, 4 ... 10, 11
# while True:
# 	counter_2 = 1
# 	while True:
# 		print(f"{counter_1} * {counter_2} = {counter_1 * counter_2}")
# 		counter_2 += 1
# 		if counter_2 > 10:
# 			break
# 	counter_1 += 1
# 	if counter_1 > 6:
# 		break


# continue
# counter_1 = 2 # 3
# counter_2 = 1 # 2, 3, 4 ... 10, 11
# while True:
# 	if counter_1 == 5:
# 		counter_1 += 1
# 		continue
# 	counter_2 = 1
# 	while True:
# 		print(f"{counter_1} * {counter_2} = {counter_1 * counter_2}")
# 		counter_2 += 1
# 		if counter_2 > 10:
# 			break
# 	counter_1 += 1
# 	if counter_1 > 6:
# 		break

# count from 1 to 10 and skip 4 to 6
# counter = 0
# while counter < 10:
# 	counter += 1
# 	if counter > 3 and counter < 7:
# 		continue
# 	print(f"{counter=}")


# truthy and falsy values
# if condition , condition => true or false
# while condition, 
# val = 0.0
# if val:
# 	print(val)


# finding the square root of a number
# a * a = b (sq root of b is a, a < b)
# num = int(input("Enter a number: "))

# for i in range(num//2):
# 	if i*i == num:
# 		print(f"square root of {num} is {i}")
# 		break


# exercise:
# 1. find if a number is prime or composite (user input)
# 2. find first n prime numbers (user inputs n)
# 3. LCM (10, 15) and HCF(x, y, z) (10, 20, 20)










