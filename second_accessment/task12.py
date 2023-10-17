# user_input = input("enter a letter")
# alphabet = 'a,e,i,o,u'
# if user_input.startswith('a'):
#     print("it's a Vowel:")
# elif user_input.startswith('e'):
#     print("It's a vowel ")
# elif user_input.startswith('i'):
#     print("Its a vowel")
# elif user_input.startswith('o'):
#     print("its a vowel")
# elif user_input.startswith('u'):
#     print("its a vowel ")
#
# else:
#     print("it's not vowel:")


import string

vowel_4 = ['a', 'e', 'i', 'o', 'u']

letter = input("Enter a letter:  ")
letter = letter.lower()

if letter in vowel_4:
    print(f'{letter} is a vowel')
else:
    print(f"{letter} is not a vowel, it is a Consonant")
