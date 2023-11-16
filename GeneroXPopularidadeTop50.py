import pandas as pd
import matplotlib.pyplot as plt
from itertools import cycle
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def gerar_grafico_popularidade_genero():
    # Importar os dados do arquivo csv
    df = pd.read_csv("spotifycharts-37i9dQZEVXbMXbN3EUUhlg.csv")

    # Calcular a distribuição das músicas por gênero
    distribuicao = df.groupby("genre").size()

    # Criar o gráfico de barras empilhadas
    plt.figure(figsize=(12, 8))

    # Usar um ciclo para repetir as cores conforme necessário
    cores = cycle(plt.rcParams['axes.prop_cycle'].by_key()['color'])

    # Iterar sobre cada gênero e plotar uma barra com uma cor diferente
    for genero, contagem in distribuicao.items():
        plt.bar(genero, contagem, color=next(cores), label=genero)

    # Adicionar um título e labels aos eixos
    plt.title("Distribuição de músicas por gênero", fontsize=17)
    plt.xlabel("Gênero", fontsize=17)
    plt.ylabel("Número de músicas", fontsize=17)

    # Ajustar o tamanho da fonte nos rótulos do eixo x
    plt.xticks(rotation=45, ha='right', fontsize=14)

    # Ajustar o tamanho da fonte nos rótulos do eixo y
    plt.yticks(fontsize=14)

    # Mover a legenda para fora do gráfico
    plt.legend(fontsize=17, bbox_to_anchor=(1, 1), loc='upper left')

    # Exibir o gráfico
    plt.tight_layout()
    plt.savefig('static/grafico2.png')
    plt.close()
    plt.show()