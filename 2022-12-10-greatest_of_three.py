# f-strings

# w.a.p to check the greatest of 3 numbers (nested if else, logical gates)

# nested if else
n1 = int(input('Enter first number: '))
n2 = int(input('Enter second number: '))
n3 = int(input('Enter third number: '))


# if n1 > n2:
# 	if n1 > n3:
# 		print(f"n1={n1} is the greatest")
# 	elif n1 < n3:
# 		print(f"n3={n3} is the greatest")
# 	else:
# 		# means n1 == n3
# 		print(f"n1={n1} & n3={n3} are the greatest")
# elif n1 < n2:
# 	if n2 > n3:
# 		print(f"n2={n2} is the greatest")
# 	elif n2 < n3:
# 		print(f"n3={n3} is the greatest")
# 	else:
# 		# means n2 == n3
# 		print(f"n2={n2} & n3={n3} are the greatest")
# else:
# 	# n1 == n2
# 	if n3 > n2:
# 		print(f"n3={n3} is the greatest")
# 	elif n3 < n2:
# 		print(f"n1={n1} & n2={n2} are the greatest")
# 	else:
# 		print(f"All the numbers are equal")

if n1>n2 and n1>n3:
	print(f"{n1=} is the greatest")
elif n2>n1 and n2>n3:
	print(f"{n2=} is the greatest")
elif n3>n1 and n3>n2:
	print(f"{n3=} is the greatest")
elif n1==n2 and n1==n3:
	print(f"All numbers are equal")
elif n1==n2 and n1>n3:
	print(f"{n1=} and {n2=} are the greatest")
elif n2==n3 and n2>n1:
	print(f"{n2=} and {n3=} are the greatest")
elif n1==n3 and n1>n2:
	print(f"{n1=} and {n3=} are the greatest")



