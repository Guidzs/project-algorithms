def is_anagram(first_string, second_string):

    if first_string == "" == second_string:
        return ("", "", False)

    first_word = list(first_string.lower())
    second_word = list(second_string.lower())

    first_string_obj = strings_analize(first_word)
    second_string_obj = strings_analize(second_word)

    first_string_orderly = string_order(first_string_obj)
    second_string_orderly = string_order(second_string_obj)

    boolean = first_string_orderly == second_string_orderly

    return (
        first_string_orderly,
        second_string_orderly,
        boolean
        )


def strings_analize(string):
    string_obj = {}

    for char in string:
        if char in string_obj:
            string_obj[char] += 1
        else:
            string_obj[char] = 1

    return string_obj


def string_order(string_obj):
    string_orderly = ''

    for char in string_obj:
        for i in range(string_obj[char]):
            string_orderly += char
    return string_orderly
