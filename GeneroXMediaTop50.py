import pandas as pd
import matplotlib.pyplot as plt
from itertools import cycle

# Carregar dados do arquivo CSV
dados = pd.read_csv('spotifycharts-37i9dQZEVXbMXbN3EUUhlg.csv')

# Calcular a popularidade média por gênero
popularidade_media_por_genero = dados.groupby('genre')['popularity'].mean().reset_index()

# Garantir que apenas os gêneros únicos presentes nos dados são usados
generos_presentes = dados['genre'].unique()
popularidade_media_por_genero = popularidade_media_por_genero[popularidade_media_por_genero['genre'].isin(generos_presentes)]

# Criar o gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(popularidade_media_por_genero['genre'], popularidade_media_por_genero['popularity'])

# Usar um ciclo para repetir as cores conforme necessário
cores = cycle(plt.rcParams['axes.prop_cycle'].by_key()['color'])

# Iterar sobre cada gênero e plotar uma barra com uma cor diferente
for index, row in popularidade_media_por_genero.iterrows():
    genero = row['genre']
    contagem = row['popularity']
    plt.bar(genero, contagem, color=next(cores), label=genero)

# Ajustar o tamanho da fonte nos rótulos do eixo x e y
plt.xlabel('Gênero', fontsize=17)
plt.ylabel('Popularidade Média', fontsize=17)

# Ajustar o tamanho da fonte nos rótulos do eixo x
plt.xticks(rotation=45, ha='right', fontsize=14)

# Ajustar o tamanho da fonte nos rótulos do eixo y
plt.yticks(fontsize=14)

# Mover a legenda para fora do gráfico
plt.legend(fontsize=17, bbox_to_anchor=(1, 1), loc='upper left')

plt.title('Popularidade Média de Músicas por Gênero', fontsize=17)

# Exibir o gráfico
plt.tight_layout()
plt.show()
