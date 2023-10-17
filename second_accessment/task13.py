def concatenate():
    list1 = ["apple,ball ,cap,"]
    list2 = ["apple,ball ,cap,"]
    list_joined = list1 + list2
    return list_joined


print(concatenate())



def concate(data_list):
    word = ""

    for element in data_list:
        word += element
    return word

if __name__ == '__main__':
    new_data = ["a", "k", "i", "n"]
    print(concate(new_data))