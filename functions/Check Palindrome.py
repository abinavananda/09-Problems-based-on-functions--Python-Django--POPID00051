def is_palindrome(s):
    return s == s[::-1]
word = "radar"
if is_palindrome(word):
    print(word, "is a palindrome.")
else:
    print(word, "is not a palindrome.")
