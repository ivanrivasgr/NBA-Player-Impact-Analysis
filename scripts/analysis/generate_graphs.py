import matplotlib.pyplot as plt
import pandas as pd
import json

# Load data from the JSON file
file_path = 'data/raw/nba_giannis_embiid_ad_stats_last_5_seasons.json'
with open(file_path, 'r') as file:
    data = json.load(file)

# Convert JSON data to a pandas DataFrame
players_data = []
for player in data:
    player_name = player['name']
    for season_stats in player['career_stats']:
        season_stats['name'] = player_name
        players_data.append(season_stats)

df = pd.DataFrame(players_data)

# Order columns for clarity
columns_order = ['name', 'SEASON_ID', 'TEAM_ABBREVIATION', 'PLAYER_AGE', 'GP', 'GS',
                 'MIN', 'PTS', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'FG_PCT', 'FG3_PCT', 'FT_PCT']
df = df[columns_order]

# Plot points per season for each player
plt.figure(figsize=(14, 8))
for player_name in df['name'].unique():
    player_data = df[df['name'] == player_name]
    plt.plot(player_data['SEASON_ID'], player_data['PTS'],
             marker='o', label=player_name)

plt.title('Points Per Season (2018-2023)')
plt.xlabel('Season')
plt.ylabel('Points')
plt.legend()
plt.grid(True)
plt.savefig('reports/figures/points_per_season.png')
plt.show()

# Plot rebounds per season for each player
plt.figure(figsize=(14, 8))
for player_name in df['name'].unique():
    player_data = df[df['name'] == player_name]
    plt.plot(player_data['SEASON_ID'], player_data['REB'],
             marker='o', label=player_name)

plt.title('Rebounds Per Season (2018-2023)')
plt.xlabel('Season')
plt.ylabel('Rebounds')
plt.legend()
plt.grid(True)
plt.savefig('reports/figures/rebounds_per_season.png')
plt.show()

# Plot assists per season for each player
plt.figure(figsize=(14, 8))
for player_name in df['name'].unique():
    player_data = df[df['name'] == player_name]
    plt.plot(player_data['SEASON_ID'], player_data['AST'],
             marker='o', label=player_name)

plt.title('Assists Per Season (2018-2023)')
plt.xlabel('Season')
plt.ylabel('Assists')
plt.legend()
plt.grid(True)
plt.savefig('reports/figures/assists_per_season.png')
plt.show()
