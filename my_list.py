my_list = []
#append 10 20 30 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
#insert 15 at 2nd pos
my_list.insert(1, 15)
#extend list[50 60 70] to my_list
my_list.extend([50, 60, 70])
#remove last element from list
my_list.pop()
#sort ascending
my_list.sort()
#find & print index of 30 in list
index_of_30 = my_list.index(30)
print("index of 30:", index_of_30)

