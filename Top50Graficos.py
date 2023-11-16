import csv
from flask import Flask, render_template, redirect, url_for
import matplotlib.pyplot as plt

app = Flask(__name__)
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def ler_dados_csv(arquivo):
    dados = []
    with open(arquivo, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Pule a primeira linha (cabeçalhos)
        for row in reader:
            dados.append({'name_track': row[0], 'popularity': float(row[1].replace(',', '.'))})
    return dados

def gerar_graficoTop50():
    dados = ler_dados_csv('Top50.csv')
    dados_ordenados = sorted(dados, key=lambda x: x['popularity'], reverse=True)
    
    posicao = range(len(dados_ordenados))
    nomes_musicas = [dado['name_track'] for dado in dados_ordenados]

    plt.figure(figsize=(10, 6))
    plt.bar(posicao, [dado['popularity'] for dado in dados_ordenados])
    plt.xlabel('Posição')
    plt.ylabel('Popularidade')
    plt.title('Músicas Mais Populares')
    plt.xticks(posicao, [dado['name_track'] for dado in dados_ordenados], rotation=90)
    plt.tight_layout()
    #plt.savefig('static/grafico.png')
    #plt.close()

    