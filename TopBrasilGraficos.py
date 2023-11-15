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

def gerar_graficoTopBrasil():
    dados = ler_dados_csv('TopBrasil.csv')
    dados_ordenados = sorted(dados, key=lambda x: x['popularity'], reverse=True)
    
    nomes_musicas = [dado['name_track'] for dado in dados_ordenados]
    popularidade = [float(dado['popularity']) for dado in dados_ordenados]

    plt.figure(figsize=(10, 6))
    plt.bar(nomes_musicas, popularidade)
    plt.xlabel('Música')
    plt.ylabel('Popularidade')
    plt.title('Músicas Mais Populares 3')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig('static/grafico3.png')
    plt.close()
