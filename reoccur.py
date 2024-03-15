from collections import Counter

def reoccur():
    # Open the existing text file containing the processed data
    with open('processed_scores.txt', 'r', encoding='utf-8') as input_file:
        processed_data = input_file.read()

    # Split the processed data into lines
    processed_lines = processed_data.strip().split('\n')

    # Use Counter to count the occurrences of each line
    line_counter = Counter(processed_lines)

    # Find the most common line and its count
    most_common_line, count = line_counter.most_common(1)[0]

    print(f"The most re-occurring line is:\n{most_common_line}\nOccurrences: {count}")
