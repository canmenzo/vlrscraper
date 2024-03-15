
# Open the existing text file containing the data
with open('scores.txt', 'r', encoding='utf-8') as input_file:
    data = input_file.read()

# Process each line and modify as needed
# Process each line and modify as needed
processed_lines = []
for line in data.strip().split('\n'):
    print("The data is being modified. Please wait...")
    match = pattern.search(line)
    if match:
        parts = line.split()
        if len(parts) >= 2:
            team, score = parts[0], parts[1]
            try:
                score1, score2 = score.split('-')
            except ValueError:
                print("Error: Unable to split score into two parts, this data is being discarded.")
                continue  # Skip this line and move to the next one
            if team == team1:
                new_line = f'{team} {score} {team2}'
            elif team == team2:
                new_line = f'{team} {score2}-{score1} {team2}'
            processed_lines.append(new_line)
        else:
            print("Error: Unable to extract team and score from the line.")
            print("Line content:", line)
    else:
        print("Error: Unable to match pattern in the line.")
        print("Line content:", line)


# Sort the processed lines based on the "team1" scores
sorted_lines = sorted(processed_lines, key=lambda x: (int(x.split()[1].split('-')[0]), int(x.split()[1].split('-')[1])))

# Open a new text file for writing the processed data
with open('processed_scores.txt', 'w', encoding='utf-8') as output_file:
    # Write the sorted lines to the file
    for line in sorted_lines:
        output_file.write(line + '\n')

print("Processed data has been exported to processed_scores.txt")


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
