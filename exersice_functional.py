from functools import reduce

my_pets=["sisi", "bibi", "titi", "carla"]

def toupper(pet):
    return pet.upper()

print(list(map(toupper, my_pets)))

my_strings = ["a", "b", "c", "d", "e"]
my_numbers = [5,4,3,2,1]

# my_numbers.sort()

#print(list(zip(my_numbers, my_strings)))

print(list(zip(my_numbers, sorted(my_strings))))

scores = [73, 20, 65, 19, 76, 100, 88]

def score(li):
    return li>50

print(list(filter(score, scores )))

# lis = scores + my_numbers
# print(lis)

def total(acc, li):
    return acc + li 

# print(reduce(total, lis, 0))
print( reduce(total, (my_numbers + scores)))