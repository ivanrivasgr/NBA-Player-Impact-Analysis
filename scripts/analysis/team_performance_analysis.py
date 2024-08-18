import pandas as pd
import matplotlib.pyplot as plt
import json
import os

# Obtener la ruta absoluta del directorio actual
current_dir = os.path.dirname(os.path.abspath(__file__))

# Definir la ruta para cargar el archivo
file_path = os.path.join(current_dir, '../../data/raw/team_stats.json')

# Cargar los datos desde el archivo JSON
with open(file_path, 'r') as file:
    data = json.load(file)

# Convertir los datos a un DataFrame de pandas
df = pd.DataFrame(data)

# Revisar las primeras filas del DataFrame para confirmar la carga de datos
print(df.head())

# Análisis de correlación entre victorias y clasificación en la conferencia con etiquetas de temporada en formato compacto
plt.figure(figsize=(10, 6))

# Iterar sobre cada equipo y agregar los datos al gráfico
for team in df['team'].unique():
    team_data = df[df['team'] == team]
    plt.scatter(team_data['wins'], team_data['conf_rank'], label=team)
    # Agregar etiquetas de temporada en formato más compacto
    for i, row in team_data.iterrows():
        season_label = row['season'][-2:] + '/' + \
            row['season'][:2]  # Formato "21/20"
        # Ajustar posición para evitar solapamientos
        plt.text(row['wins'] + 0.1, row['conf_rank'] -
                 0.2, season_label, fontsize=9)

plt.title('Victorias vs Clasificación en la Conferencia')
plt.xlabel('Victorias en Temporada Regular')
plt.ylabel('Clasificación en la Conferencia')
plt.gca().invert_yaxis()  # Invertir el eje Y para que 1 sea el más alto
plt.legend(title="Equipos")
plt.grid(True)
plt.savefig(os.path.join(
    current_dir, '../../reports/figures/wins_vs_conf_rank.png'))
plt.show()


# Análisis por equipo específico - Milwaukee Bucks (Giannis Antetokounmpo)
bucks_data = df[df['team'] == 'Milwaukee Bucks']

plt.figure(figsize=(10, 6))
plt.plot(bucks_data['season'], bucks_data['wins'],
         marker='o', label='Victorias')
plt.title('Victorias de Milwaukee Bucks por Temporada')
plt.xlabel('Temporada')
plt.ylabel('Victorias en Temporada Regular')
plt.legend()
plt.grid(True)
plt.savefig(os.path.join(
    current_dir, '../../reports/figures/bucks_wins_by_season.png'))
plt.show()

# Análisis por equipo específico - Philadelphia 76ers (Joel Embiid)
sixers_data = df[df['team'] == 'Philadelphia 76ers']

plt.figure(figsize=(10, 6))
plt.plot(sixers_data['season'], sixers_data['wins'],
         marker='o', label='Victorias')
plt.title('Victorias de Philadelphia 76ers por Temporada')
plt.xlabel('Temporada')
plt.ylabel('Victorias en Temporada Regular')
plt.legend()
plt.grid(True)
plt.savefig(os.path.join(
    current_dir, '../../reports/figures/sixers_wins_by_season.png'))
plt.show()

# Análisis por equipo específico - Los Angeles Lakers (Anthony Davis)
lakers_data = df[df['team'] == 'Los Angeles Lakers']

plt.figure(figsize=(10, 6))
plt.plot(lakers_data['season'], lakers_data['wins'],
         marker='o', label='Victorias')
plt.title('Victorias de Los Angeles Lakers por Temporada')
plt.xlabel('Temporada')
plt.ylabel('Victorias en Temporada Regular')
plt.legend()
plt.grid(True)
plt.savefig(os.path.join(
    current_dir, '../../reports/figures/lakers_wins_by_season.png'))
plt.show()
