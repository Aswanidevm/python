#map ,filter, zip and reduce
# pure function doesnt affect the ouside world
my_list = [2,3,5,7,1,6]
def multi_by2(li):
    # newlist=[]
    # for item in li:
    #     newlist.append(item*2)
    # return newlist
    return li*2

# print(multi_by2([3,2,5,4,6,1]))
#map
print(list(map(multi_by2, my_list)))
li1 = map(multi_by2, my_list)

# filter 

def onlyodd(li):
    return li % 2 != 0

print(list(filter(onlyodd, my_list)))
li2 = filter(onlyodd, my_list)
# zip will make a tuple with  variable from the concerned list
print(list(zip(li1,li2)))
#zip

#reduce is not in python bultin function

from functools import reduce # imports from the the function. 

def accumulator(acc, li):
    print (acc, li)
    return acc + li

print(reduce(accumulator, my_list, 0))
    

