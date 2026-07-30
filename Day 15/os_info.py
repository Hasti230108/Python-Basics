import os

print("Current Folder:")
print(os.getcwd())

print("\nFiles:")

for file in os.listdir():
    print(file)