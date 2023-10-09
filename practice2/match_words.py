def match_words(letters):
    count = 0
    for letter in letters:
        if len(letter) > 1 and letter[0] == letter[-1]:
            count += 1
    return count


print(match_words(['abc', 'xyz', 'aba', '1222']))

