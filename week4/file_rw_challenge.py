import os

# Ask the user for the filename to read
filename = input("Enter the filename to read: ")

try:
    # Attempt to read the file
    with open(filename, 'r') as f:
        content = f.read()
except FileNotFoundError:
    print("Error: The file does not exist.")
except PermissionError:
    print("Error: Permission denied to read the file.")
except Exception as e:
    print(f"Error reading the file: {e}")
else:
    # If successful, modify the content (for example, reverse the text)
    modified_content = content[::-1]
    
    # Ask for the new filename to write the modified content
    new_filename = input("Enter the new filename to write the modified version: ")
    
    try:
        # Write the modified content to the new file
        with open(new_filename, 'w') as f:
            f.write(modified_content)
        print("Modified file written successfully.")
    except Exception as e:
        print(f"Error writing the file: {e}")
