str1 = '/*Jon is @developer & Musician!'
for symbol in str1:
    for character in symbol:
        if character in '/*@!':
            str1 = str1.replace(symbol, "")
print(str1)

# def special_symbol(str1):
#     for i in str1:
#         for j in i:
#             if j in '/*@!':
#                 str1 = str1.replace(i)
#         print(str1)
#
#
#         str1 = '/*Jon is @developer & Musician!'
#         special_symbol(str1)
