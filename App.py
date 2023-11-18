from flask import Flask, render_template, redirect, url_for
from GeneroXMediaTop50 import gerar_grafico_popularidade_media_por_genero_Top50
from GeneroXPopularidadeTop50 import gerar_grafico_popularidade_genero_Top50
from VariacaoPopularidadeTop50 import gerar_grafico_variacao_popularidade_Top50
from PopularidadeXArtistaTop50 import gerar_grafico_popularidade_artista_Top50
from DuracaoMusicasTop50 import gerar_grafico_duracao_musicas_Top50
from DanceabilityXEnergyTop50 import gerar_grafico_danceability_energy_Top50

from GeneroXMediaTop100 import gerar_grafico_popularidade_media_por_genero_Top100
from GeneroXPopularidadeTop100 import gerar_grafico_popularidade_genero_Top100
from VariacaoPopularidadeTop100 import gerar_grafico_variacao_popularidade_Top100
from PopularidadeXArtistaTop100 import gerar_grafico_popularidade_artista_Top100
from DuracaoMusicasTop100 import gerar_grafico_duracao_musicas_Top100
from DanceabilityXEnergyTop100 import gerar_grafico_danceability_energy_Top100

from GeneroXMediaTopBrasil import gerar_grafico_popularidade_media_por_genero_TopBrasil
from GeneroXPopularidadeTopBrasil import gerar_grafico_popularidade_genero_TopBrasil
from VariacaoPopularidadeTopBrasil import gerar_grafico_variacao_popularidade_TopBrasil
from PopularidadeXArtistaTopBrasil import gerar_grafico_popularidade_artista_TopBrasil
from DuracaoMusicasTopBrasil import gerar_grafico_duracao_musicas_TopBrasil
from DanceabilityXEnergyTopBrasil import gerar_grafico_danceability_energy_TopBrasil

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', grafico1=False, grafico2=False, grafico3=False, grafico4=False, grafico5=False, grafico6=False, grafico7=False, grafico8=False, grafico9=False, grafico10=False, grafico11=False, grafico12=False, grafico13=False, grafico14=False, grafico15=False, grafico16=False, grafico17=False, grafico18=False)

@app.route('/grafico')
def exibir_grafico():
    return render_template('grafico.html')

@app.route('/gerar_graficoTop50')
def gerar_e_mostrar_grafico():
    gerar_grafico_popularidade_media_por_genero_Top50()
    gerar_grafico_popularidade_genero_Top50()
    gerar_grafico_variacao_popularidade_Top50()
    gerar_grafico_popularidade_artista_Top50()
    gerar_grafico_duracao_musicas_Top50()
    gerar_grafico_danceability_energy_Top50()
    return render_template('grafico.html', grafico1=True, grafico2=True, grafico3=True, grafico4=True, grafico13=True, grafico16=True)

@app.route('/gerar_graficoTop100')
def gerar_e_mostrar_grafico2():
    gerar_grafico_popularidade_media_por_genero_Top100()
    gerar_grafico_popularidade_genero_Top100()
    gerar_grafico_variacao_popularidade_Top100()
    gerar_grafico_popularidade_artista_Top100()
    gerar_grafico_duracao_musicas_Top100()
    gerar_grafico_danceability_energy_Top100()
    return render_template('grafico.html', grafico5=True, grafico6=True, grafico7=True, grafico8=True, grafico14=True, grafico17=True)

@app.route('/gerar_graficoTopBrasil')
def gerar_e_mostrar_grafico3():
    gerar_grafico_popularidade_media_por_genero_TopBrasil()
    gerar_grafico_popularidade_genero_TopBrasil()
    gerar_grafico_variacao_popularidade_TopBrasil()
    gerar_grafico_popularidade_artista_TopBrasil()
    gerar_grafico_duracao_musicas_TopBrasil()
    gerar_grafico_danceability_energy_TopBrasil()
    return render_template('grafico.html', grafico9=True, grafico10=True, grafico11=True, grafico12=True, grafico15=True, grafico18=True)

if __name__ == '__main__':
    app.run(debug=True)
