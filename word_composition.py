import time

# Function to check if a word is a compounded word
def is_compound(word, word_set, memo):
    if word in memo:
        return memo[word]
    if word in word_set:
        memo[word] = True
        return True
    for i in range(1, len(word)):
        if word[:i] in word_set and word[i:] in word_set:
            memo[word] = True
            return True
    memo[word] = False
    return False

# Function to process the input file
def process_file(file_name):
    start_time = time.perf_counter()

    # Reading the input file
    with open(file_name, 'r') as file:
        words = [line.strip() for line in file.readlines()]

    # Debugging: Print first 10 words for verification
    print(f"Words in {file_name}: {words[:10]}...")

    word_set = set(words)
    compound_words = []
    memo = {}

    # Finding compound words
    for word in words:
        if is_compound(word, word_set, memo):
            compound_words.append(word)

    # Sorting compound words by length in descending order
    compound_words.sort(key=len, reverse=True)

    longest = compound_words[0] if compound_words else ""
    second_longest = compound_words[1] if len(compound_words) > 1 else ""

    # Calculating time taken
    end_time = time.perf_counter()
    time_taken = (end_time - start_time) * 1000  # milliseconds

    # Displaying the result
    print(f"Longest Compound Word: {longest}")
    print(f"Second Longest Compound Word: {second_longest}")
    print(f"Time taken to process file {file_name}: {time_taken:.3f} milli seconds")

# Running the program for Input_01.txt and Input_02.txt
process_file('Input_01.txt')  # For smaller file
process_file('Input_02.txt')  # For larger file