word = input("Enter a string: ")
w = word.lower()
count = 0

for letter in w:
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        count += 1

print("Number of vowels in the string:", count)