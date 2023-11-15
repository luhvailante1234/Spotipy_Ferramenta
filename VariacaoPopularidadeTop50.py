import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # Importar Seaborn para utilizar paleta de cores

# Importar os dados do arquivo csv
df = pd.read_csv("spotifycharts-37i9dQZEVXbMXbN3EUUhlg.csv")

# Converter a coluna 'date' para o tipo datetime
df['date_collected'] = pd.to_datetime(df['date_collected'])

# Escolher uma data específica (substitua '2023-01-01' pela data desejada)
data_especifica = '2023-11-14'
df_data_especifica = df[df['date_collected'] == data_especifica]

# Criar uma paleta de cores
colors = sns.color_palette('viridis', len(df_data_especifica))

# Criar o gráfico de linha com pontos coloridos
plt.figure(figsize=(12, 6))
plt.scatter(df_data_especifica['name_track'], df_data_especifica['popularity'], c=colors, label='Popularidade')

# Adicionar um título e labels aos eixos
plt.title(f"Popularidade das Músicas em {data_especifica}", fontsize=17)
plt.xlabel("Música", fontsize=17)
plt.ylabel("Popularidade", fontsize=17)

# Ajustar o tamanho da fonte nos rótulos do eixo x
plt.xticks(rotation=45, ha='right', fontsize=12)

# Ajustar o tamanho da fonte nos rótulos do eixo y
plt.yticks(fontsize=12)

# Adicionar legenda
plt.legend()

# Ajustar o layout do gráfico
plt.tight_layout()

# Exibir o gráfico
plt.show()
