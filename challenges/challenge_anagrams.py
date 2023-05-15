def is_anagram(first_string, second_string):

    if first_string == "" == second_string:
        return ("", "", False)

    first_word = list(first_string.lower())
    second_word = list(second_string.lower())

    first_string_orderly = ''.join(string_order(first_word))
    second_string_orderly = ''.join(string_order(second_word))

    boolean = first_string_orderly == second_string_orderly

    return (
        first_string_orderly,
        second_string_orderly,
        boolean
        )


# def strings_analize(string):
#     string_obj = {}

#     for char in string:
#         if char in string_obj:
#             string_obj[char] += 1
#         else:
#             string_obj[char] = 1

#     return string_obj


def string_order(string):
    if len(string) <= 1:
        return string

    initial = string[0]
    left = []
    right = []
    for char in string[1:]:
        if char <= initial:
            left.append(char)
        else:
            right.append(char)
    return string_order(left) + [initial] + string_order(right)
