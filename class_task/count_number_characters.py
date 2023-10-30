# str1 = 'google.com'
# unique_element = {}
#
# for i in str1:
#     if i in unique_element:
#         unique_element[i] += 1
#     else:
#         unique_element[i] = 1
#
# print(str(unique_element))


def character_frequency(words: str):
    # result = {}
    # for character in words:
    #     if character in result.keys():
    #         result[character] += 1
    #     else:
    #         result[character] = 1
    # return result
    return {word: words.count(word) for word in words}


print(character_frequency('bible'))
