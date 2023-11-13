def adding_to_string(input1):
    length = len(input1)
    if length >= 3:
        if input1[3:] == 'ing':
            input1 += 'ly'
        else:
            input1 += 'ing'

    return input1


print(adding_to_string("abc"))
print(adding_to_string("string"))
print(adding_to_string("it"))
print(adding_to_string("favour"))
print(adding_to_string("erring"))
