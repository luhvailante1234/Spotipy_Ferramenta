from flask import Flask, render_template, redirect, url_for
from Top50Graficos import gerar_graficoTop50
from Top100Graficos import gerar_graficoTop100
from TopBrasilGraficos import gerar_graficoTopBrasil

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', grafico1=False, grafico2=False, grafico3=False)

@app.route('/grafico')
def exibir_grafico():
    return render_template('grafico.html')

@app.route('/gerar_graficoTop50')
def gerar_e_mostrar_grafico():
    gerar_graficoTop50()
    return redirect(url_for('exibir_grafico', filename='top50.html'))

@app.route('/gerar_graficoTop100')
def gerar_e_mostrar_grafico2():
    gerar_graficoTop100()
    return redirect(url_for('exibir_grafico'))

@app.route('/gerar_graficoTopBrasil')
def gerar_e_mostrar_grafico3():
    gerar_graficoTopBrasil()
    return redirect(url_for('exibir_grafico'))

if __name__ == '__main__':
    app.run(debug=True)
