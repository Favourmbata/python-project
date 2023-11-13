def return_three_letter(input1):
    length = len(input1)
    if input1 >= 3:
        if input1[3:] == 'ing':
            input1 += 'ly'
    else:
        input1 += 'ing'

    return input1
