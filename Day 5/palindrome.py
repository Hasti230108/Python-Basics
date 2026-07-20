def ReverseString(word):
    reverse_word = ""

    for letter in word:
        reverse_word = letter + reverse_word
    
    return reverse_word

word = input("Enter a string: ")
reverse_word = ReverseString(word)

if word == reverse_word:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")