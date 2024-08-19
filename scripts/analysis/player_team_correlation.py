import os
import pandas as pd
import matplotlib.pyplot as plt

# Dictionary to map abbreviations to full team names
team_name_mapping = {
    'MIL': 'Milwaukee Bucks',
    'PHI': 'Philadelphia 76ers',
    'NOP': 'New Orleans Pelicans',
    'LAL': 'Los Angeles Lakers'
}

# Custom colors for each player
player_color_mapping = {
    'Giannis Antetokounmpo': 'green',
    'Joel Embiid': 'blue',
    'Anthony Davis': 'yellow'
}

# Load player and team data
current_dir = os.path.dirname(os.path.abspath(__file__))
player_file_path = os.path.join(
    current_dir, '../../data/raw/nba_giannis_embiid_ad_stats_last_5_seasons.json')
team_file_path = os.path.join(current_dir, '../../data/raw/team_stats.json')

with open(player_file_path, 'r') as file:
    player_data = pd.read_json(file)

# Extract player career stats and organize them into a DataFrame
players_stats = []
for _, row in player_data.iterrows():
    player_name = row['name']
    for stats in row['career_stats']:
        stats['name'] = player_name
        players_stats.append(stats)

players_df = pd.DataFrame(players_stats)
players_df = players_df.rename(
    columns={'SEASON_ID': 'season', 'TEAM_ABBREVIATION': 'team'})
players_df['season'] = players_df['season'].apply(lambda x: x.split('-')[0])
players_df['season'] = players_df['season'].astype(str)
players_df['team'] = players_df['team'].map(team_name_mapping)

with open(team_file_path, 'r') as file:
    team_data = pd.read_json(file)

team_data['season'] = team_data['season'].apply(lambda x: x.split('-')[0])
team_data['season'] = team_data['season'].astype(str)

# Merge player and team data by season and team
merged_df = pd.merge(players_df, team_data, on=['season', 'team'], how='inner')

if not merged_df.empty:
    plt.figure(figsize=(10, 6))
    for player_name in merged_df['name'].unique():
        player_data = merged_df[merged_df['name'] == player_name]
        plt.scatter(player_data['PTS'], player_data['wins'], label=f'{player_name}',
                    color=player_color_mapping[player_name])
        for i, season in enumerate(player_data['season']):
            plt.text(player_data['PTS'].iloc[i],
                     player_data['wins'].iloc[i], season, fontsize=9)

    plt.title('Player Impact (Points) on Team Wins')
    plt.xlabel('Player Points per Season')
    plt.ylabel('Team Wins in Regular Season')
    plt.legend(title="Players")
    plt.grid(True)
    plt.savefig(os.path.join(
        current_dir, '../../reports/figures/player_impact_on_team_wins_colored.png'))
    plt.show()
else:
    print("The 'merged_df' DataFrame is empty, cannot generate charts.")
