import requests

from bs4 import BeautifulSoup
import pandas as pd
import time

# URL of the website to scrape
url = "https://www.vlr.gg/312765/karmine-corp-vs-funplus-phoenix-champions-tour-2024-masters-madrid-swiss-stage-r1"

# Send an HTTP GET request to the website
response = requests.get(url)

# Parse the HTML code using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the relevant information from the HTML code
games = []
for row in soup.select('div.post-container'):
  for row in soup.select('div.div.threading'):
    score = row.find('div', class_='post-body').find('p').get_text()
    games.append([score])

# Store the information in a pandas dataframe
df = pd.DataFrame(games)

# Add a delay between requests to avoid overwhelming the website with requests
time.sleep(1)

# Export the data to a CSV file
df.to_csv('score.txt', sep='\t', index=False)