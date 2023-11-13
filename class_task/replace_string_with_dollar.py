def split(input1):
    for word in range(len(input1)-1):
        if input1[word][0] == input1[word + 1][0]:
            input1[word] = input1[word].capitalize()
    return input1