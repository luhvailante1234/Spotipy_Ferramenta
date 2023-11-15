import csv
import matplotlib.pyplot as plt

def ler_dados_csv(arquivo):
    dados = []
    with open(arquivo, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Pule a primeira linha (cabeçalhos)
        for row in reader:
            dados.append({'name_track': row[0], 'popularity': float(row[1].replace(',', '.'))})
    return dados

def gerar_grafico():
    dados = ler_dados_csv('Top50.csv')
    dados_ordenados = sorted(dados, key=lambda x: x['popularity'], reverse=True)
    
    posicao = range(len(dados_ordenados))
    nomes_musicas = [dado['name_track'] for dado in dados_ordenados]

    plt.figure(figsize=(10, 6))
    plt.plot(posicao, nomes_musicas)
    plt.xlabel('Posição')
    plt.ylabel('Nome da Música')
    plt.title('Músicas Mais Populares')
    plt.xticks(posicao, [dado['name_track'] for dado in dados_ordenados], rotation=90)
    plt.tight_layout()
    plt.savefig('static/grafico.png')
    plt.close()
