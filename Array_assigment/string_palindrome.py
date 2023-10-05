def is_palindrome(stri):
    return stri == stri[:: -1]


stri = "boy"
ans = is_palindrome(stri)
if ans:
    print("yes it palindrome")
else:
    print("no! it not palindrome")
