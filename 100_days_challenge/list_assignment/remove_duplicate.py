
lst = [15, 20, 25, 20, 10, 5]

duplicate_item = set()
for i in lst:
    if i not in duplicate_item:
        duplicate_item.add(i)

print(duplicate_item)
