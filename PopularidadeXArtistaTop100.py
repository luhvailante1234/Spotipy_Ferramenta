import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from itertools import cycle
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def gerar_grafico_popularidade_artista_Top100():
    # Importar os dados do arquivo csv
    df = pd.read_csv("spotifycharts-5YRmjoCTiI6uPGJAevX87A.csv")

    # Calcular a popularidade dos artistas
    popularidade = df.groupby("name_artist").size().reset_index(name='contagem')

    # Ordenar por contagem em ordem decrescente e pegar os 10 primeiros
    popularidade = popularidade.sort_values(by='contagem', ascending=False).head(10)

    # Criar o gráfico de barras
    plt.figure(figsize=(12, 6))
    
    # Usar um ciclo para repetir as cores conforme necessário
    cores = cycle(sns.color_palette('viridis', len(popularidade)))

    # Criar o gráfico de barras horizontais
    for i, (artista, contagem) in enumerate(zip(popularidade['name_artist'], popularidade['contagem'])):
        plt.barh(artista, contagem, color=next(cores), label=artista)

    # Adicionar um título e labels aos eixos
    plt.title("Top 10 Artistas mais Populares", fontsize=17)
    plt.xlabel("Popularidade", fontsize=17)
    plt.ylabel("Artista", fontsize=17)

    # Ajustar o tamanho da fonte nos rótulos do eixo x
    plt.xticks(ha='right', fontsize=12)

    # Ajustar o tamanho da fonte nos rótulos do eixo y
    plt.yticks(fontsize=12)

    # Adicionar legenda com as cores fora do gráfico
    plt.legend(fontsize=10,title='Legenda', bbox_to_anchor=(1.05, 1), loc='upper left')

    # Salvar o gráfico como imagem
    plt.tight_layout()
    plt.savefig('static/grafico8.png')
    plt.close()
