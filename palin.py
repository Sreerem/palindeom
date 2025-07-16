 palindrome.py
# A simple program to check if a word is a palindrome

def is_palindrome(word: str) -> bool:
    # Remove spaces and convert to lowercase
    cleaned = word.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

# Ask user for input
text = input("Enter a word: ")

# Check and print result
if is_palindrome(text):
    print(f"✅ '{text}' is a palindrome!")
else:
    print(f"❌ '{text}' is not a palindrome.")
