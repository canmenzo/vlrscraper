import re

def clean():
    # Open the existing text file containing the data
    with open('output.txt', 'r', encoding='utf-8') as input_file:
        data = input_file.read()

    # Open a new text file for writing cleaned data
    with open('scores.txt', 'w', encoding='utf-8') as output_file:
        # Split the data into lines
        lines = data.strip().split('\n')
        # Regular expression to match lines containing "team1" or "team2" followed by a number
        pattern = re.compile(r'(team1|team2)\s[012]-[012]')

        # Loop through each line, filter and write to the file
        for line in lines:
            print("The data is being cleaned. Please wait...")
            match = pattern.search(line)
            if match:
                filtered_line = match.group()
                output_file.write(filtered_line + '\n')

    print("Filtered data has been exported to scores.txt")
