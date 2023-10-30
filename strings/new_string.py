str1 = "James"

first_index = str1[0]

temp = len(str1)
divide = int(temp / 2)

first_index = first_index + str1[divide]
first_index = first_index + str1[temp - 1]
print(first_index)