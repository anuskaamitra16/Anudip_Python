#write a function in python to count and display the total number of words in a text file "ABC.txt"

def write_to_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)
        
# Create the file and write some content
file_path = "ABC.txt"
sample_content = """Line 1: Hello, this is the first line.
Line 2: This is the second line.
Line 3: Last line."""
write_to_file(file_path, sample_content)

# Read and print the content

def read_file_and_count_words(file_path):
    word_count = 0

    with open(file_path, 'r') as file:
        # Read each line
        for line in file:
            words = line.split()  # Split the line into words
            word_count += len(words)  # Add the number of words in the line to the total count

            # Print the line
            print(line.strip())

    print(f"\nNumber of words in the file: {word_count}")

read_file_and_count_words(file_path)

#Output
'''
Line 1: Hello, this is the first line.
Line 2: This is the second line.
Line 3: Last line.

Number of words in the file: 19
'''




