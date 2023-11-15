import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.patches import Patch

# Importar os dados do arquivo csv
df = pd.read_csv("spotifycharts-37i9dQZEVXbMXbN3EUUhlg.csv")

# Converter a coluna 'date' para o tipo datetime
df['date_collected'] = pd.to_datetime(df['date_collected'])

# Escolher uma data específica (substitua '2023-01-01' pela data desejada)
data_especifica = '2023-11-15'
df_data_especifica = df[df['date_collected'] == data_especifica]

# Selecionar as 10 músicas mais populares
top_10 = df_data_especifica.nlargest(10, 'popularity')

# Criar uma paleta de cores
colors = sns.color_palette('viridis', len(top_10))

# Criar o gráfico de dispersão com legenda de cores
plt.figure(figsize=(12, 6))
scatter = plt.scatter(top_10['name_track'], top_10['popularity'], c=colors, label='Popularidade')

# Adicionar quadrados coloridos à legenda
legend_handles = [Patch(color=color, label=name) for name, color in zip(top_10['name_track'], colors)]

# Adicionar legenda com as 10 músicas mais populares fora do gráfico
plt.legend(handles=legend_handles, title='Legenda', bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=10, title_fontsize=12)

# Adicionar um título e labels aos eixos
plt.title(f"Top 10 Músicas Mais Populares em {data_especifica}", fontsize=17)
plt.xlabel("Música", fontsize=17)
plt.ylabel("Popularidade", fontsize=17)

# Ajustar o tamanho da fonte nos rótulos do eixo x
plt.xticks(rotation=45, ha='right', fontsize=12)

# Ajustar o tamanho da fonte nos rótulos do eixo y
plt.yticks(fontsize=12)

# Ajustar o layout do gráfico
plt.tight_layout()

# Exibir o gráfico
plt.show()