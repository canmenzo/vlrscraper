



team1 = ""
team2 = ""



def new_clean(team1, team2):
    with open('output.txt', 'r', encoding='utf-8') as input_file:
        data = input_file.read()

    # Open a new text file for writing cleaned data
    with open('zort.txt', 'w', encoding='utf-8') as output_file:
        # Regular expression to match lines containing "team1" or "team2" followed by a number
        zort = re.search(fr'(.*\b({team1}|{team2}).*\s*[012])|(\s*[012].*\b({team1}|{team2}).*)', re.IGNORECASE)
        for line in input_file:
            match = zort.search(line)
            if match:
                output_file.write(filtered_line + '\n')
    print("Filtered data has been exported to scores.txt")