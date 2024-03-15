import requests
import re
from bs4 import BeautifulSoup
import time

def scrape():
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
            #
            print("The data is being scraped. Please wait...")
            # Add a delay between requests to avoid overwhelming the website with requests
            # time.sleep(1)
            # Print or process the content of each <p> tag
            for p_tag in p_tags:
                file.write(p_tag.get_text() + '\n')

    print("Data has been exported to output.txt")