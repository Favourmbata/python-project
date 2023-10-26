sample_list = [1, 3, 2, 5, 3, 4, 6, 4, 6, 9, 8, 2, 10, 8, 12, 10, 4, 6, 14]
def unique_list(lst):
    # new_list = ()
    # for even_numbers in lst:
    #     if even_numbers % 2 == 0:
    #         new_list.__add__(even_numbers)
    #
    # return new_list
    return {i for i in lst if i % 2 == 0}


print(unique_list(sample_list))

