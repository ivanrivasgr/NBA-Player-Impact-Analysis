import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL de la página que queremos scrapear
url = "https://www.basketball-reference.com/leagues/NBA_2024_per_game.html"

# Realizar la solicitud HTTP a la URL
response = requests.get(url)

# Analizar el contenido HTML de la página
soup = BeautifulSoup(response.content, 'html.parser')

# Encontrar la tabla con las estadísticas de los jugadores
table = soup.find('table', {'id': 'per_game_stats'})

# Leer la tabla en un DataFrame de pandas
df = pd.read_html(str(table))[0]

# Mostrar las primeras filas del DataFrame
print(df.head())

# Guardar el DataFrame en un archivo CSV
df.to_csv('nba_player_stats_2024.csv', index=False)
