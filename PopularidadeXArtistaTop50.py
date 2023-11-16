import pandas as pd
import matplotlib.pyplot as plt
from itertools import cycle

def gerar_grafico_popularidade_artista():
    # Importar os dados do arquivo csv
    df = pd.read_csv("spotifycharts-37i9dQZEVXbMXbN3EUUhlg.csv")

    # Calcular a popularidade dos artistas
    popularidade = df.groupby("name_artist").size().reset_index(name='contagem')

    # Ordenar por contagem em ordem decrescente e pegar os 10 primeiros
    popularidade = popularidade.sort_values(by='contagem', ascending=False).head(10)

    # Criar o gráfico de barras horizontais
    cores = cycle(plt.rcParams['axes.prop_cycle'].by_key()['color'])
    for i, (artista, contagem) in enumerate(zip(popularidade['name_artist'], popularidade['contagem'])):
        plt.barh(artista, contagem, color=next(cores), label=artista)

    # Adicionar um título e labels aos eixos
    plt.title("Top 10 Artistas mais Populares", fontsize=17)
    plt.xlabel("Popularidade", fontsize=17)
    plt.ylabel("Artista", fontsize=17)

    # Ajustar o tamanho da fonte nos rótulos do eixo x
    plt.xticks(fontsize=14)

    # Ajustar o tamanho da fonte nos rótulos do eixo y
    plt.yticks(fontsize=14)

    # Mover a legenda para fora do gráfico
    plt.legend(fontsize=12, bbox_to_anchor=(1, 1), loc='upper left')

    # Ajustar o layout do gráfico
    plt.tight_layout()

    # Ajustar a posição da legenda
    plt.subplots_adjust(right=0.8)

    # Exibir o gráfico
    plt.show()
