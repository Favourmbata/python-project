# def remove_duplicate(item):
#     duplicate = set[]
#     unique_lst = []
#
#     for x in item:
#         if x not in item:
#             unique_lst.append(x)
#             duplicate

lst = [15, 20, 25, 20, 10, 5]

duplicate_item = set()
unique_item = []
for i in lst:
    if i not in duplicate_item:
        unique_item.append(i)
        duplicate_item.add(i)

print(duplicate_item)
