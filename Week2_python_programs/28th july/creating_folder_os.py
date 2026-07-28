#creating folder using os
import os

filename = "sam.txt"

# Create the file
with open(filename, "w") as file:
    file.write("Hi how r u!")

print("File created successfully.")

#path
print("File Path:", os.path.abspath(filename))