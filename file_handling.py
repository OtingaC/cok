# Question 1. Program that reads file and writes modified version to new file.
def file_read_write():
    try:
        with open("input.txt", "r") as infile:
            content = infile.read()

# Write to a new file
        with open("output.txt", "w") as outfile:
            outfile.write(content)

        print("File read and modified content written to output.txt")

    except FileNotFoundError:
        print("input.txt not found. Please create file first.")


# Question 2. Ask user for filename and handle errors if doesn’t exist or can’t be read.
def error_handling():
    filename = input("Enter a filename to open")
    try:
        with open(filename, "r") as f:
            print("File opened succesfully!")
            print(f.read())
    except FileNotFoundError:
        print("File does not exist.")
    except PermissionError:
        print("You don't have permission to read this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")



if __name__ == "__main__":
    print("\n--- Running File ---")
    file_read_write()

    print("\n--- Running Error---")
    error_handling()