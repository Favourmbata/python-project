my_list = [[0, 0, 0],
           [0, 0, 0]]

# my_list[1][2] = 5
for idx, val in enumerate(my_list):
    word = list(enumerate(my_list))
print(word)

temperatures = {
    'Monday': [66, 70, 74],
    'Tuesday': [50, 56, 64],
    'Wednesday': [75, 80, 83],
    'Thursday': [67, 74, 81]
}
for k, v in temperatures.items():
    print(f'{k}: {sum(v) / len(v):.2f}')
