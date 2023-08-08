class SuperList(list):
    def __init__(self, i):
        self.i =i
        print(i)
    def __len__(self):
        return 1000
    
super_list1 = SuperList(1, 2, 3)
print(len(super_list1))
# super_list1.append(5)
print(super_list1[0])