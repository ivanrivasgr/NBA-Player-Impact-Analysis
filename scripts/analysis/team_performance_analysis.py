import pandas as pd
import matplotlib.pyplot as plt
import json
import os

# Get the absolute path of the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Define the path to load the file
file_path = os.path.join(current_dir, '../../data/raw/team_stats.json')

# Load data from the JSON file
with open(file_path, 'r') as file:
    data = json.load(file)

# Convert the data into a pandas DataFrame
df = pd.DataFrame(data)

# Check the first few rows of the DataFrame to confirm data loading
print(df.head())

# Correlation analysis between wins and conference rank with compact season labels
plt.figure(figsize=(10, 6))

# Iterate over each team and add the data to the plot
for team in df['team'].unique():
    team_data = df[df['team'] == team]
    plt.scatter(team_data['wins'], team_data['conf_rank'], label=team)
    # Add season labels in a more compact format
    for i, row in team_data.iterrows():
        season_label = row['season'][-2:] + '/' + \
            row['season'][:2]  # Format "21/20"
        # Adjust position to avoid overlaps
        plt.text(row['wins'] + 0.1, row['conf_rank'] -
                 0.2, season_label, fontsize=9)

plt.title('Wins vs Conference Rank')
plt.xlabel('Regular Season Wins')
plt.ylabel('Conference Rank')
plt.gca().invert_yaxis()  # Invert Y-axis so 1 is the highest
plt.legend(title="Teams")
plt.grid(True)
plt.savefig(os.path.join(
    current_dir, '../../reports/figures/wins_vs_conf_rank.png'))
plt.show()

# Analysis for specific team - Milwaukee Bucks (Giannis Antetokounmpo)
bucks_data = df[df['team'] == 'Milwaukee Bucks']

plt.figure(figsize=(10, 6))
plt.plot(bucks_data['season'], bucks_data['wins'], marker='o', label='Wins')
plt.title('Milwaukee Bucks Wins per Season')
plt.xlabel('Season')
plt.ylabel('Regular Season Wins')
plt.legend()
plt.grid(True)
plt.savefig(os.path.join(
    current_dir, '../../reports/figures/bucks_wins_by_season.png'))
plt.show()

# Analysis for specific team - Philadelphia 76ers (Joel Embiid)
sixers_data = df[df['team'] == 'Philadelphia 76ers']

plt.figure(figsize=(10, 6))
plt.plot(sixers_data['season'], sixers_data['wins'], marker='o', label='Wins')
plt.title('Philadelphia 76ers Wins per Season')
plt.xlabel('Season')
plt.ylabel('Regular Season Wins')
plt.legend()
plt.grid(True)
plt.savefig(os.path.join(
    current_dir, '../../reports/figures/sixers_wins_by_season.png'))
plt.show()

# Analysis for specific team - Los Angeles Lakers (Anthony Davis)
lakers_data = df[df['team'] == 'Los Angeles Lakers']

plt.figure(figsize=(10, 6))
plt.plot(lakers_data['season'], lakers_data['wins'], marker='o', label='Wins')
plt.title('Los Angeles Lakers Wins per Season')
plt.xlabel('Season')
plt.ylabel('Regular Season Wins')
plt.legend()
plt.grid(True)
plt.savefig(os.path.join(
    current_dir, '../../reports/figures/lakers_wins_by_season.png'))
plt.show()
