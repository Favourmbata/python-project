# create a tuple
t = ('Jim', 'Ben', 'Tom', 'Zack')
# convert the tuple to list
ls = list(t)
# swap the elements in the list using their index
ls[0], ls[3] = ls[3], ls[0]
# create a new tuple from the list elements
new_t = tuple(ls)
# print the new tuple
print(new_t)
#

item = 15, 25, 60, 50, 30, 40, 45, 55
lt = list(item)

lt[0], lt[7] = lt[7], lt[0]
lt.append(item)
new_item = lt[0], lt[7]

print(tuple(new_item))


