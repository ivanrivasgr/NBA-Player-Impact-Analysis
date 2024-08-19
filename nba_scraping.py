import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the page to scrape
url = "https://www.basketball-reference.com/leagues/NBA_2024_per_game.html"

# Send HTTP request to the URL
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table with player statistics
table = soup.find('table', {'id': 'per_game_stats'})

# Read the table into a pandas DataFrame
df = pd.read_html(str(table))[0]

# Display the first few rows of the DataFrame
print(df.head())

# Save the DataFrame to a CSV file
df.to_csv('nba_player_stats_2024.csv', index=False)
