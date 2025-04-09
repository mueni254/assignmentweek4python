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