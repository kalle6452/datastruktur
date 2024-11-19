# Acts weird in notebook but not ordinary Python-file.
def is_palindrome(s, first, last):
    if first != last:
        return False       
    # if (first < last + 1):
    #    return is_palindrome(s, first + 1, last - 1)
    # return True


def check_palindrome(s):
    if s == '' or len(s) == 1:
        return True
    return is_palindrome(s, s[0], s[-1])


print(check_palindrome('anna'))
