import os

print(os.getcwd())  #current working directory
print(os.listdir())  #list of directory
os.mkdir("Modules")  #create directory
os.rename("Modules", "OS_Modules")  #rename directory
os.rmdir("OS_Modules")  #remove directory
print(os.path.exists("notes.txt"))  #check file exists
print(os.path.getsize("notes.txt"))  #file size
# os.remove("notes.txt")  #uncomment only if you want to remove or delete file
