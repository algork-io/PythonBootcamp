# # Sets

# # myset1 = {"item1","item2","item3"}
# # # print(myset1)
# # myset = set(('a','b'))
# # for i in myset1:
# # 	print(i)




# # Tuples

# # tup1 = ('item1','item2',)


# dict1 = {'key1':1,'key2':2,'key3':4}
# # print(type(dict1))

# # for item in dict1.items():
# # 	print(item)

# # for item in dict1.values():
# # 	print(item)

# # for item in dict1.keys():
# # 	print(item)



# # for key,values in dict1.items():
# # 	print(key,values)


# item1 = dict1['key3']
# item1 = dict1.get('key5')

# print(dict1.values())

# a = dict1.pop('key2')
# print(a,dict1)
# dict1['key2'] = 10
# print(dict1)

# a = {'a':[1,2,3,4,5],'b':[{}]}



# Create a dictionary from string, where keys are
# the index of the characters (starting from 0) 
# and values are the characters at the indices



# w.a.p which will increment a list of integers by 1

# def incr(l):
# 	for i in range(len(l)):
# 		l[i] +=1
# 	return l


list1 = [1,2,3,4,5]

# res = incr(list1)
# print(res)



# def incr(l):
# 	return l+1

# res = list(map(incr,list1))
# print(res)


# res = list(map(lambda l:l+1,list1))
# print(res)

# def test(var):
# 	if var in ['a','e','i']:
# 		return True
# 	else:
# 		return False


l1 = ['b','c','d',1,2]

# filt = list(filter(test,a))
# print(filt)


# a,b,*c = l1

# print(a,b,c)




