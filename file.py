# Answer part 1
def read_and_write_file():
    try:
        # Open the file to read
        with open('input.txt', 'r') as input_file:
            content = input_file.read()

        # Modify the content (e.g., convert to uppercase)
        modified_content = content.upper()

        # Write to a new file
        with open('output.txt', 'w') as output_file:
            output_file.write(modified_content)

        print("File has been read and modified successfully!")
    except FileNotFoundError:
        print("Error: The file 'input.txt' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function
read_and_write_file()


# Answer Part 2
def handle_file_errors():
    filename = input("Enter the filename to read: ")
    try:
        # Try to open the file
        with open(filename, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to read '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Call the function
handle_file_errors()
