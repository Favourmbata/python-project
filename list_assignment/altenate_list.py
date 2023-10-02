def alternate_list(lst1, lst2):
    return [sub[item] for item in range(len(lst2))
            for sub in [lst1, lst2]]


lst1 = [1, 2, 3]
lst2 = ['a','b','c']
print(alternate_list(lst1,lst2))