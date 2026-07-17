print("To know whether the letter is vowel or consonant")
letter = input("Enter a letter:")
l = letter.lower()

if (l == 'a' or l == 'e' or l == 'i' or l == 'o' or l =='u'):
    print(letter, "is a vowel.")
else:
    print(letter, "is a consonant.")