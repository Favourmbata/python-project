def roman_figure(figure: str) -> int:
    num = 0
    roman_figures = {'I': 1,
                     'V': 5,
                     'X': 10,
                     'L': 50,
                     }
    for i in range(len(figure)):
        char = figure[i].capitalize()
        num += roman_figures[char]
    return num


print(roman_figure('i'))
print(roman_figure('ii'))
print(roman_figure('vi'))
print(roman_figure('v'))
print(roman_figure('x'))
print(roman_figure('xv'))
print(roman_figure('l'))
print(roman_figure('xiii'))
