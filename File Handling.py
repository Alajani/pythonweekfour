def file_modifier():
    try:
        # Ask user for input and output filenames
        input_file = input("Enter the name of the file to read: ")
        output_file = input("Enter the name of the file to write to: ")

        # Attempt to open and read the input file
        with open(input_file, 'r') as infile:        
            data = infile.readlines()

        # Modify the content (example: convert to uppercase)
        modified_data = [line.upper() for line in data]

        # Write the modified content to the output file
        with open(output_file, 'w') as outfile:
            outfile.writelines(modified_data)

        print(f"File processed successfully! Modified content written to {output_file}.")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist. Please check the filename and try again.")
    except PermissionError:
        print(f"Error: Permission denied for accessing '{input_file}' or '{output_file}'.") 
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the program
file_modifier()
