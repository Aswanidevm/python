#map ,filter, zip and reduce
# pure function doesnt affect the ouside world
def multi_by2(li):
    # newlist=[]
    # for item in li:
    #     newlist.append(item*2)
    # return newlist
    return li*2

# print(multi_by2([3,2,5,4,6,1]))
#map
print(list(map(multi_by2, [2,3,4])))