#Renaming a file with os
import os

filename = "hi.txt"

with open(filename, "w") as file:
    file.write("Hello, Python!")

print("File created successfully.")

# Rename 
new_filename = "bye.txt"
os.rename(filename, new_filename)

print("File renamed successfully.")

# Display path
print("File Path:", os.path.abspath(new_filename))