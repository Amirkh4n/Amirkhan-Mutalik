def is_palindrome(word):
    return word == word[::-1]

word = input("Enter a word or phrase: ").replace(" ", "")

print(f"The word or phrase '{word}' is {'a palindrome' if is_palindrome(word) else 'not a palindrome'}.")
