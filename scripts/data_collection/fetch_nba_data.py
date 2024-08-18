from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats
import json
import os

# Define the players of interest
player_names = ['Giannis Antetokounmpo', 'Joel Embiid', 'Anthony Davis']

# Get all NBA players
nba_players = players.get_players()

# Define the seasons you want to collect data for (last 5 seasons)
seasons = ['2018-19', '2019-20', '2020-21', '2021-22', '2022-23']

all_stats = []

for name in player_names:
    # Select the player by name
    player = next((p for p in nba_players if p['full_name'] == name), None)

    if player:
        player_stats = {
            'name': player['full_name'],
            'id': player['id'],
            'career_stats': {}
        }

        # Fetch career stats for the player
        career_stats = playercareerstats.PlayerCareerStats(
            player_id=player['id'])
        stats_df = career_stats.get_data_frames()[0]

        # Filter stats for the selected seasons
        filtered_stats = stats_df[stats_df['SEASON_ID'].isin(seasons)]

        # Include team abbreviation to track team changes
        player_stats['career_stats'] = filtered_stats[['SEASON_ID', 'TEAM_ABBREVIATION', 'PLAYER_AGE', 'GP', 'GS',
                                                       'MIN', 'PTS', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'FG_PCT', 'FG3_PCT', 'FT_PCT']].to_dict('records')

        all_stats.append(player_stats)
    else:
        print(f"Player {name} not found.")

# Save all data to a JSON file
raw_data_path = os.path.join(
    '..', '..', 'data', 'raw', 'nba_giannis_embiid_ad_stats_last_5_seasons.json')
with open(raw_data_path, 'w') as f:
    json.dump(all_stats, f)

print(f"Data saved to {raw_data_path}")
