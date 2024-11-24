# Acts weird in notebook but not ordinary Python-file.
def is_palindrome(s, first, last):
    # base condition
    if s[first] != s[last]:
        return False
    # If string has length 0 or 1 it is always palindrome.abs
    # If first and last character are equal and length is 2
    # it is also palindrome.
    if s[first] == s[last] and len(s) <= 2:
        return True
    # Removing first and last letter.
    s = s[(first+1):]
    s = s[:last]
    # Performing recursive step
    return is_palindrome(s, first, last)


def check_palindrome(s):
    # always palindrome if string has length 0 or 1.
    if s == '' or len(s) == 1:
        return True
    return is_palindrome(s, 0, -1)


print(check_palindrome('abcdefedcba'))
