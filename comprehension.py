mylist =[]

# for item in "hello":
#     mylist.append(item )

#list comprehention

mylist=[char for char in "hello"]
mylist1= [num for num in range(1,10)]
mylist2= [num**2 for num in range(1,10)]
mylist3= [num**2 for num in range(1,10) if num%2 ==0]

print(mylist3)


#set comprehension

myset={char for char in "hello"}
myset1= {num for num in range(1,10)}
myset2= {num**2 for num in range(1,10)}

print(myset2)


# dictionary

# my_dict = {
#     "name" : "aswa",
#     "pass" : "dev"

# }

# print(my_dict)
li = [1, 2, 3]
mydic= {num: num*2 for num in li}
print(mydic)


somelist = ["a", "b", "c", "b", "d", "m", "m", "n", "n"]

# duplicate =[]
# for item in somelist:
#     if somelist.count(item) >1:
#         if item not in duplicate:
#             duplicate.append(item)

duplicate= [ somelist.count>]