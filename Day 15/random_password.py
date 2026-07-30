import random

characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"

password = "" 

for i in range(10):
    password += random.choice(characters)

psd = input("\nTry to enter password(10 characters only):")

if psd == password:
    print("Right Guess.")
else:
    print("Wrong Guess.")
    print(f"Password: {password}")