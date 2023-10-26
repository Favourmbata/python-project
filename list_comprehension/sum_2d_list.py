def sum_column(nums1, num2):
    result = sum(row[num2] for row in nums1)
    return result


first_list = [[1, 2, 3, 2],
              [4, 5, 6, 2],
              [7, 8, 9, 5]]
print("original list of lists:")
print(first_list)

column = 0
print("\n sum:ist column of the said list of list:")
print(sum_column(first_list, column))

column = 1
print("\n sum:2nd column of the said list of list:")
print(sum_column(first_list, column))

column = 3
print("\n sum:fourth column of the said list of list:")

print(sum_column(first_list, column))
