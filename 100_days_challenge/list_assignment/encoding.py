letters = 'abcdefghijklmnopqrstuvwxyz'
num_letters = len(letters)


# def encrypting(plain_text, key):
#     cipher_text = ''
#     for letter in plain_text:
#         letter = letter.lower()
#         if not letter == ' ':
#             index = letters.find(letter)
#             if index == -1:
#                 cipher_text += letter
#             else:
#                 new_index = index + key
#                 if new_index >= num_letters:
#                     new_index -= num_letters
#                 cipher_text += letters[new_index]
#     return cipher_text


# def decrypting(cipher_text, key):
#     plain_text = ''
#     for letter in cipher_text:
#         letter = letter.lower()
#         if not letter == ' ':
#             index = letters.find(letter)
#             if index == -1:
#                 plain_text += letter
#         else:
#             new_index = index - key
#             if new_index < 0:
#                 new_index += num_letters
#             plain_text += letters[new_index]
#     return plain_text
def encrypt_decrypt(text, mode, key):
    result = ''
    if mode == 'd':
        key = - key

    for letter in text:
        letter = letter.lower()
        if not letter == ' ':
            index = letters.find(letter)
            if index == -1:
                result += letter
            else:
                new_index = index + key
            if new_index >= num_letters:
                new_index -= num_letters
            elif new_index < 0:
                new_index += num_letters
            result += letters[new_index]
    return result


print()
print('**** CEASER CIPHER ****')
print()
print('Do you want to Encrypt or Decrypt?')
user_input = input('E or D: ').lower()
print()
if user_input == 'e':
    print('ENCRYPTION MODE SELECTED')
    print()
    key = int(input("Enter the key(1 through 26):"))
    text = input("enter the text to encrypt: ")
    cipher_text = encrypt_decrypt(text, user_input, key)
    print(f'CIPHERTEXT:{cipher_text}')

elif user_input == 'd':
    print('DECRYPTION MODE SELECTED')
    print()
    key = int(input('Enter the key (1 through 26):'))
    text = input("Enter the text to decrypt: ")
    plain_text = encrypt_decrypt(text, user_input, key)
    print(f"PLAINTEXT:{plain_text}")
