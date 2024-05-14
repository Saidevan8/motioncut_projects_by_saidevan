def count_words(fname):
    """
    This function takes a string as input and returns the number of words in the string.
    """
    with open(fname) as f:
        word_count=0
        for i in f:
            # Remove any leading or trailing whitespace
            i = i.strip()
            # Check if the input is empty
            if not i:
                return 0
            # Split the string into words using whitespace as the delimiter
            words = i.split()
            # adding the number of words in the line to a variable word_count
            word_count+=len(words)
        return word_count

# Get user input as file
fname='word_counter.txt'
# Count the number of words
word_count = count_words(fname)
# Print the word count
print("The number of words in the input is:", word_count)
