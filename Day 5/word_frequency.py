word = input("Enter a string:")

checked = ""

for letter in word:
    if letter not in checked:
        count = 0
        for ch in word:
            if letter == ch:
                count += 1
        
        print(letter, "=", count)
        checked += letter