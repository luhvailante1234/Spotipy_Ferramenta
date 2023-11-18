import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def gerar_grafico_duracao_musicas_TopBrasil():
    # Leitura do arquivo CSV
    df = pd.read_csv('spotifycharts-37i9dQZF1DX0FOF1IUWK1W.csv')

    # Extraindo a coluna de duração das músicas e convertendo para segundos
    duracao_musica_segundos = df['duration_ms'] / 1000

    # Criando o histograma
    plt.figure(figsize=(12, 6))

    # Usar a mesma paleta de cores do primeiro gráfico
    cores = sns.color_palette('magma', 20)

    n, bins, patches = plt.hist(duracao_musica_segundos, bins=20, edgecolor='black')

    # Atribuir cores diferentes a cada barra do histograma
    for i in range(len(patches)):
        patches[i].set_facecolor(cores[i])

    # Adicionando rótulos e título ao gráfico
    plt.xlabel('Duração da Música (segundos)', fontsize=17)
    plt.ylabel('Frequência', fontsize=17)
    plt.title('Duração das Músicas', fontsize=17)

    # Ajustar o tamanho da fonte nos rótulos do eixo x
    plt.xticks(ha='right', fontsize=12)

    # Ajustar o tamanho da fonte nos rótulos do eixo y
    plt.yticks(fontsize=12)

    # Salvar o gráfico como imagem
    plt.tight_layout()
    plt.savefig('static/grafico15.png')

    # Fechar a figura após salvar
    plt.close()
