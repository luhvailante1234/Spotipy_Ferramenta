import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from itertools import cycle
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def gerar_grafico_popularidade_media_por_genero_Top100():
    # Carregar dados do arquivo CSV
    dados = pd.read_csv('spotifycharts-5YRmjoCTiI6uPGJAevX87A.csv')

    # Calcular a popularidade média por gênero
    popularidade_media_por_genero = dados.groupby('genre')['popularity'].mean().reset_index()

    # Garantir que apenas os gêneros únicos presentes nos dados são usados
    generos_presentes = dados['genre'].unique()
    popularidade_media_por_genero = popularidade_media_por_genero[popularidade_media_por_genero['genre'].isin(generos_presentes)]

    # Criar o gráfico de barras
    plt.figure(figsize=(12, 6))

    # Usar um ciclo para repetir as cores conforme necessário
    cores = cycle(sns.color_palette('viridis', len(popularidade_media_por_genero)))

    # Iterar sobre cada gênero e plotar uma barra com uma cor diferente
    for genero, popularidade in zip(popularidade_media_por_genero['genre'], popularidade_media_por_genero['popularity']):
        plt.bar(genero, popularidade, color=next(cores), label=genero)

    # Adicionar um título e labels aos eixos
    plt.title('Popularidade Média de Músicas por Gênero', fontsize=17)
    plt.xlabel('Gênero', fontsize=17)
    plt.ylabel('Popularidade Média', fontsize=17)

    # Ajustar o tamanho da fonte nos rótulos do eixo x
    plt.xticks(rotation=45, ha='right', fontsize=12)

    # Ajustar o tamanho da fonte nos rótulos do eixo y
    plt.yticks(fontsize=12)

    # Adicionar legenda com as cores fora do gráfico
    plt.legend(fontsize=10,title='Legenda', bbox_to_anchor=(1.05, 1), loc='upper left')

    # Salvar o gráfico como imagem
    plt.tight_layout()
    plt.savefig('static/grafico5.png')
    plt.close()
