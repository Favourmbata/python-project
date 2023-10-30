def get_counted_element(str1):
    unique_element = {}
    for character in str1:
        if character in unique_element:
            unique_element[character] += 1
        else:
            unique_element[character] = 1
            return str(unique_element)
