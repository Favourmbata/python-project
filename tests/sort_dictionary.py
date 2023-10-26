import operator

#
sample_input = {2: 4, 1: 1, 3: 9, 5: 25, 4: 16}
sort = dict(sorted(sample_input.items()))
print(sort)

sample_one = {0: 10, 1: 20}
print(sample_one)

sample_one[2] = 30
print(sample_one)


# def add_key_value(dictionary, key, value):
#     dictionary[key] = value
#     return dictionary
#
#
# print(add_key_value(sample_input), 6, 36)

# sample_input = {2: 4, 1: 1, 3: 9, 5: 25, 4: 16}
#
#
# def sort_sample_dict(sample_dict):
#     for key1 in sample_input.keys():
#         for key2 in sample_input.keys():
#             if sample_input[key1] > sample_input[key2]:
#                 sample_input[key1], sample_input[key2] = sample_input
#                 sort_dict = dict(sorted(sample_input.items()))
#
#     print(sort_dict)
