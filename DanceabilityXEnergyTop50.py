import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def gerar_grafico_danceability_energy_Top50():
    # Leitura do arquivo CSV
    df = pd.read_csv('spotifycharts-37i9dQZEVXbMXbN3EUUhlg.csv')

    # Criando o gráfico de dispersão
    plt.figure(figsize=(12, 6))

    # Usar a mesma paleta de cores do primeiro gráfico
    cores = sns.color_palette('viridis', len(df))

    # Plotar o gráfico de dispersão
    scatter = plt.scatter(df['danceability'], df['energy'], c=cores, edgecolor='black', alpha=0.7)

    # Adicionando rótulos e título ao gráfico
    plt.xlabel('Danceability', fontsize=17)
    plt.ylabel('Energy', fontsize=17)
    plt.title('Relação entre Danceability e Energy', fontsize=17)

    # Ajustar o tamanho da fonte nos rótulos do eixo x
    plt.xticks(fontsize=12)

    # Ajustar o tamanho da fonte nos rótulos do eixo y
    plt.yticks(fontsize=12)

    # Adicionar legenda com as cores fora do gráfico
    handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=cores[i], markersize=10) for i in range(len(df))]
    plt.legend(handles, df['name_track'], title='Legenda', fontsize=10, title_fontsize=12, bbox_to_anchor=(1.05, 1), loc='upper left')

    # Salvar o gráfico como imagem
    plt.tight_layout()
    plt.savefig('static/grafico16.png', bbox_inches='tight')

    # Fechar a figura após salvar
    plt.close()
