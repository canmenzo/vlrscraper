import requests
from bs4 import BeautifulSoup
import time
import re
from collections import Counter

# URL of the website to scrape
print("Welcome to the VLR scraper")
url = input("\nPlease enter the VLR URL for the game:")
team1 = input("\nPlease enter the first team:")
team2 = input("\nPlease enter the second team:")

# Send an HTTP GET request to the website
response = requests.get(url)

# Create a BeautifulSoup object
soup = BeautifulSoup(response.content, 'html.parser')

# Find all instances of div with class "post-body"
post_bodies = soup.find_all('div', class_='post-body')

# Loop through each post body and extract all <p> tags
with open('output.txt', 'w', encoding='utf-8') as file:
    for post_body in post_bodies:
        p_tags = post_body.find_all('p')
        print("The data is being scraped. Please wait...")
        # Add a delay between requests to avoid overwhelming the website with requests
        time.sleep(1)
        # Print or process the content of each <p> tag
        for p_tag in p_tags:
            file.write(p_tag.get_text() + '\n')

print("Data has been exported to output.txt")

# Open the existing text file containing the data
with open('output.txt', 'r', encoding='utf-8') as input_file:
    data = input_file.read()

# Open a new text file for writing cleaned data
with open('scores.txt', 'w', encoding='utf-8') as output_file:
    # Regular expression to match lines containing "team1" or "team2" followed by a number
    pattern = re.compile(fr'(.*\b({team1}|{team2}).*\s*[012])|(\s*[012].*\b({team1}|{team2}).*)', re.IGNORECASE)

    # Loop through each line, filter and write to the file
    for line in data.strip().split('\n'):
        print("The data is being cleaned. Please wait...")
        match = pattern.search(line)
        if match:
            filtered_line = match.group()
            output_file.write(filtered_line + '\n')

print("Filtered data has been exported to scores.txt")

# Open the existing text file containing the data
with open('scores.txt', 'r', encoding='utf-8') as input_file:
    data = input_file.read()

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
