def is_palindrome_non_recusive(word: str):
    """Return True if word is a palindrome, False if not."""
    return word == word[::-1]

def is_palindrome_recursive(word: str):
    if len(word) <= 1:
        return True
    else:
        return word[0] == word[-1] and is_palindrome_recursive(word[1:-1])

# Examples
print(is_palindrome_non_recusive('foo'))
print(is_palindrome_non_recusive('racecar'))
print(is_palindrome_non_recusive('troglodyte'))
print(is_palindrome_non_recusive('civic'))


