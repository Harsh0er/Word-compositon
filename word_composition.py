import time

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

def process_file(file_name):
    start_time = time.perf_counter()
 
    with open(file_name, 'r') as file:
        words = [line.strip() for line in file.readlines()]
   
    print(f"Words in {file_name}: {words[:10]}...")

    word_set = set(words)
    compound_words = []
    memo = {}

    
    for word in words:
        if is_compound(word, word_set, memo):
            compound_words.append(word)

   
    compound_words.sort(key=len, reverse=True)

    longest = compound_words[0] if compound_words else ""
    second_longest = compound_words[1] if len(compound_words) > 1 else ""

    
    end_time = time.perf_counter()
    time_taken = (end_time - start_time) * 1000  # milliseconds

    
    print(f"Longest Compound Word: {longest}")
    print(f"Second Longest Compound Word: {second_longest}")
    print(f"Time taken to process file {file_name}: {time_taken:.3f} milli seconds")


process_file('Input_01.txt')  # For smaller file
process_file('Input_02.txt')  # For larger file
