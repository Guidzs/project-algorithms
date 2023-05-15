def is_palindrome_iterative(word):
    if word == '':
        return False

    palindrome = ''
    for i in range((len(word) - 1), -1, -1):
        palindrome += word[i]

    return palindrome == word
