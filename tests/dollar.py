def covert_string_to_dollar(dollar: str):
    first_letter = dollar[0]
    dollar = dollar.replace(first_letter, "$")

    return first_letter + dollar[1:]
