
print("===== TEXT ANALYZER =====")

text = input("Enter a sentence: ")

if text == "":
    print("Please enter some text.")

else:
    words = text.split()

    print("\n===== RESULT =====")
    print("Your text:", text)
    print("Total characters:", len(text))
    print("Total words:", len(words))
    print("Uppercase:", text.upper())
    print("Lowercase:", text.lower())

    print("\n===== WORD LIST =====")

    for word in words:
        print(word)

    print("\nAnalysis completed!")
