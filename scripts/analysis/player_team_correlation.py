import os
import pandas as pd
import matplotlib.pyplot as plt

# Diccionario de abreviaturas a nombres completos
team_name_mapping = {
    'MIL': 'Milwaukee Bucks',
    'PHI': 'Philadelphia 76ers',
    'NOP': 'New Orleans Pelicans',
    'LAL': 'Los Angeles Lakers'
}

# Colores personalizados para cada jugador
player_color_mapping = {
    'Giannis Antetokounmpo': 'green',
    'Joel Embiid': 'blue',
    'Anthony Davis': 'yellow'
}

# Cargar los datos de los jugadores y equipos
current_dir = os.path.dirname(os.path.abspath(__file__))
player_file_path = os.path.join(
    current_dir, '../../data/raw/nba_giannis_embiid_ad_stats_last_5_seasons.json')
team_file_path = os.path.join(current_dir, '../../data/raw/team_stats.json')

# Cargar datos de jugadores
with open(player_file_path, 'r') as file:
    player_data = pd.read_json(file)

# Extraer las estadísticas de carrera de los jugadores y organizarlas en un DataFrame
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

# Convertir el campo de temporada a string para asegurar la consistencia
players_df['season'] = players_df['season'].astype(str)

# Mapear las abreviaturas de los equipos a nombres completos
players_df['team'] = players_df['team'].map(team_name_mapping)

# Cargar datos de equipos
with open(team_file_path, 'r') as file:
    team_data = pd.read_json(file)

# Ajustar el formato de las temporadas en los datos de equipos
team_data['season'] = team_data['season'].apply(lambda x: x.split('-')[0])
team_data['season'] = team_data['season'].astype(str)

# Fusionar los datos por temporada y equipo
merged_df = pd.merge(players_df, team_data, on=['season', 'team'], how='inner')

# Verificar el contenido de merged_df
print("Merged DataFrame:", merged_df.head())

# Si el DataFrame `merged_df` no está vacío, generamos el gráfico de dispersión
if not merged_df.empty:
    plt.figure(figsize=(10, 6))
    for player_name in merged_df['name'].unique():
        player_data = merged_df[merged_df['name'] == player_name]
        plt.scatter(player_data['PTS'], player_data['wins'], label=f'{player_name}',
                    color=player_color_mapping[player_name])
        for i, season in enumerate(player_data['season']):
            plt.text(player_data['PTS'].iloc[i],
                     player_data['wins'].iloc[i], season, fontsize=9)

    plt.title('Impacto del Jugador (Puntos) en las Victorias del Equipo')
    plt.xlabel('Puntos del Jugador por Temporada')
    plt.ylabel('Victorias del Equipo en Temporada Regular')
    plt.legend(title="Jugadores")
    plt.grid(True)
    plt.savefig(os.path.join(
        current_dir, '../../reports/figures/player_impact_on_team_wins_colored.png'))
    plt.show()

else:
    print("El DataFrame 'merged_df' está vacío, no se pueden generar gráficos.")
