from flask import Flask, render_template, redirect, url_for
from GeneroXMediaTop50 import gerar_grafico_popularidade_media_por_genero_Top50
from GeneroXPopularidadeTop50 import gerar_grafico_popularidade_genero_Top50
from VariacaoPopularidadeTop50 import gerar_grafico_variacao_popularidade_Top50
from PopularidadeXArtistaTop50 import gerar_grafico_popularidade_artista_Top50
from GeneroXMediaTop100 import gerar_grafico_popularidade_media_por_genero_Top100
from GeneroXPopularidadeTop100 import gerar_grafico_popularidade_genero_Top100
from VariacaoPopularidadeTop100 import gerar_grafico_variacao_popularidade_Top100
from PopularidadeXArtistaTop100 import gerar_grafico_popularidade_artista_Top100
from GeneroXMediaTopBrasil import gerar_grafico_popularidade_media_por_genero_TopBrasil

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', grafico1=False, grafico2=False, grafico3=False)

@app.route('/grafico')
def exibir_grafico():
    return render_template('grafico.html')

@app.route('/gerar_graficoTop50')
def gerar_e_mostrar_grafico():
    gerar_grafico_popularidade_media_por_genero_Top50()
    gerar_grafico_popularidade_genero_Top50()
    gerar_grafico_variacao_popularidade_Top50()
    gerar_grafico_popularidade_artista_Top50()
    return render_template('grafico.html', grafico1=True, grafico2=True, grafico3=True, grafico4=True)

@app.route('/gerar_graficoTop100')
def gerar_e_mostrar_grafico2():
    gerar_grafico_popularidade_media_por_genero_Top100()
    gerar_grafico_popularidade_genero_Top100()
    gerar_grafico_variacao_popularidade_Top100()
    gerar_grafico_popularidade_artista_Top100()
    return render_template('grafico.html', grafico5=True, grafico6=True, grafico7=True, grafico8=True)

if __name__ == '__main__':
    app.run(debug=True)
