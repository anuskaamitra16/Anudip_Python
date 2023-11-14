#Write a function in python to read the content from a text file "ABC.txt" line by line.

def write_to_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

def read_file_line_by_line(file_path):
    with open(file_path, 'r') as file:
        # Read and print each line
        for line in file:
            print(line.strip())  # strip() is used to remove leading and trailing whitespaces

# Create the file and write some content
file_path = "ABC.txt"
sample_content = """Line 1: Hello, this is the first line.
Line 2: This is the second line.
Line 3: Last line."""
write_to_file(file_path, sample_content)

# Read and print the content
read_file_line_by_line(file_path)

#Output
'''
Line 1: Hello, this is the first line.
Line 2: This is the second line.
Line 3: Last line.
'''
