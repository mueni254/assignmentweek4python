# Step 1: Read the original file
with open("soma.txt", "r") as original:
    content = original.read()

# Step 2: Modify the content
# Here we are simply appending a line to the content
modified_content = content + "\nWell we can modify this file"

# Step 3: Write to a new file
# We will write the modified content to a new file called "soma_modified.txt"
# This will create a new file if it doesn't exist or overwrite it if it does
with open("soma_modified.txt", "w") as modified:
    modified.write(modified_content)

print("Modified content has been written to 'soma_modified.txt'")

# Ask the user for a filename and handle errors if it doesn’t exist or can’t be read

def read_file():
    filename = input("Please enter the filename: ")
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("\nFile contents:\n")
            print(content)
    except FileNotFoundError:
        print(f"\nError: The file '{filename}' was not found.")
    except PermissionError:
        print(f"\nError: Permission denied. Cannot read the file '{filename}'.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

# Call the function
read_file()



