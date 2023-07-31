# # methods vs function
# # lists()
# # print()
# # max()
# # min()
# # input()

# # def randomstuff():
# #     pass
# # randomstuff()

# #methods
# # starts with '.''
# # methods are owned by the left of the "."

# # docstring

# '''
# can comment define for function
# '''
# def isodd(num):
#     # if num % 2 ==0:
#     #     return False
#     # else:
#     #     return True
#     return num % 2 ==0

# print(isodd(6))

# *args **kwargs(keyword arguments)

# def highest_even(li):
#     even = []
#     for i in range(len(li)):
#         if li[i] % 2 == 0:
#             even.append(li[i])
#     return max(even)
# print(highest_even([10,2,3,4,8,12]))

def highest_even(li):
     even = []
     for i in li:
          if i % 2 == 0:
               even.append(i)
     return max(even)

print(highest_even([10,2,3,4,8,12]))