def ReverseString(word):
    reverse_word = ""

    for letter in word:
        reverse_word = letter + reverse_word
    
    return reverse_word

word = input("Enter a string: ")

print("Original string:", word)
print("Reversed string:", ReverseString(word))