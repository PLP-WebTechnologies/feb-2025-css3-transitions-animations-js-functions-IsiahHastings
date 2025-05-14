def read_and_modify_file():
    # Ask user for the input filename
    filename = input("Enter the name of the file to read: ")

    try:
        # Try to open the file for reading
        with open(filename, 'r') as file:
            content = file.read()

        # Modify content (e.g., convert to uppercase)
        modified_content = content.upper()

        # Write to a new file
        new_filename = "modified_" + filename
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)

        print(f"Modified content written to '{new_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except IOError as e:
        print(f"An error occurred while reading or writing files: {e}")

# Run the program
read_and_modify_file()
