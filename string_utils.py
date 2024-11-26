# string_utils.py

def capitalize_words(sentence):
    """
    Capitalizes the first letter of each word in a sentence.
    It takes the input string as the parameter "sentence" and returns a string with each letter capitalized
    """
    return ' '.join(word.capitalize() for word in sentence.split())


def is_palindrome(word):
    """
    Checks if a word is a palindrome (reads the same forward and backward).
    return True if the word is a palindrome, False otherwise
    """
    cleaned = ''.join(char.lower() for char in word if char.isalnum())
    return cleaned == cleaned[::-1]


def generate_random_password(length=8):
    """
    Generates a random password with a mix of letters, digits, and special characters.
    :return: A randomly generated password
    """
    import random
    import string

    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    return ''.join(random.choice(chars) for _ in range(length))


if __name__ == "__main__":
    "Using the functions"
    print(capitalize_words("hello world from python"))
    print(is_palindrome("A man a plan a canal Panama"))
    print(generate_random_password(12))
