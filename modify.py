import re

def modify():
    # Open the existing text file containing the data
    with open('scores.txt', 'r', encoding='utf-8') as input_file:
        data = input_file.read()

    # Regular expression to match lines containing "team1" or "team2" followed by a number
    pattern = re.compile(r'(team1|team2)\s([012])-([012])')

    # Process each line and modify as needed
    processed_lines = []
    for line in data.strip().split('\n'):
        print("The data is being modified. Please wait...")
        match = pattern.search(line)
        if match:
            team, score1, score2 = match.groups()
            if team == 'team1':
                new_line = f'{line} team2'
            elif team == 'team2':
                new_line = f'team1 {score2}-{score1} team2'
            processed_lines.append(new_line)

    # Sort the processed lines based on the "team1" scores
    sorted_lines = sorted(processed_lines, key=lambda x: (int(x.split()[1].split('-')[0]), int(x.split()[1].split('-')[1])))

    # Open a new text file for writing the processed data
    with open('processed_scores.txt', 'w', encoding='utf-8') as output_file:
        # Write the sorted lines to the file
        for line in sorted_lines:
            output_file.write(line + '\n')

    print("Processed data has been exported to processed_scores.txt")