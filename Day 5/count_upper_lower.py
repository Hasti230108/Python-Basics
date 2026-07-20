word = input("Enter a string: ")
upper_count = 0
lower_count = 0

for letter in word:
    if letter.isupper():
        upper_count += 1
    elif letter.islower():
        lower_count += 1

print("Number of uppercase letters in the string:", upper_count)
print("Number of lowercase letters in the string:", lower_count)