list1 = ['3', '5', '7', '23']
tuple1 = '3', '4', '7', '23'

print(list1)
print(tuple1)

sequence = input("Enter a list of numbers separating them with a comma:  ")
list_generated = sequence.split(",")
tuple_generated = tuple(list_generated)

print(f'List: {list_generated}\nTuple: {tuple_generated}')
