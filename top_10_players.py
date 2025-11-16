import pandas as pd
df = pd.read_csv('players_per_game_stats.csv')
df = df.drop_duplicates(subset=['Player'], keep='first')
df2 = df.head(10)
df2.to_csv('top10_players.csv', index=False)