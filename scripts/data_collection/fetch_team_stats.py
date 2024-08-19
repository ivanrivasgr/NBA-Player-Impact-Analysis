from nba_api.stats.endpoints import teamyearbyyearstats, teamgamelog
import pandas as pd
import os

# Team IDs
teams = {
    "Milwaukee Bucks": 1610612749,
    "Philadelphia 76ers": 1610612755,
    "New Orleans Pelicans": 1610612740,
    "Los Angeles Lakers": 1610612747
}

# Seasons of interest
seasons = ['2018-19', '2019-20', '2020-21', '2021-22', '2022-23']

all_team_data = []

for team_name, team_id in teams.items():
    team_stats = teamyearbyyearstats.TeamYearByYearStats(
        team_id=team_id).get_data_frames()[0]
    team_season_data = team_stats[team_stats['YEAR'].isin(seasons)]

    for index, row in team_season_data.iterrows():
        season = row['YEAR']
        wins = row['WINS']
        losses = row['LOSSES']
        conf_rank = row['CONF_RANK']

        # Get game logs for the current season
        game_log = teamgamelog.TeamGameLog(
            team_id=team_id, season=season).get_data_frames()[0]
        playoff_games = game_log[game_log['MATCHUP'].str.contains(
            ' vs ', case=False)]
        playoff_results = playoff_games[playoff_games['MATCHUP'].str.contains(
            'Playoffs', case=False)]

        all_team_data.append({
            "team": team_name,
            "season": season,
            "wins": wins,
            "losses": losses,
            "conf_rank": conf_rank,
            "playoff_results": playoff_results[['GAME_DATE', 'MATCHUP', 'WL', 'PTS', 'REB', 'AST']].to_dict('records') if not playoff_results.empty else "No playoffs data"
        })

# Save data to a JSON file
current_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(current_dir, '../../data/raw/team_stats.json')
os.makedirs(os.path.dirname(data_path), exist_ok=True)

with open(data_path, 'w') as f:
    pd.DataFrame(all_team_data).to_json(f, orient='records', indent=4)

print(f"Data saved to {data_path}")
