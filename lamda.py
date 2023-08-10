#lamda expressions
# lambda param: param(action)
from functools import reduce
my_list = [1,2,3,4,5]
# print(list(map(lambda item: item*2, my_list)))

# print(list(filter(lambda item: item % 2 != 0, my_list)))

# print(reduce(lambda accu, item: item+accu, my_list))

print(list(map(lambda item: item**2, my_list)))

# list sorting
a = [(0,2), (4,3), (9,9), (10, -1)]
a.sort(key=lambda x: x[1])
print(a)
# print(tuple(map(lambda item: sorted(my_list, key = 2), my_list)))


