from flask import Flask, render_template
from grafico1 import gerar_grafico
from grafico2 import gerar_grafico2
from grafico3 import gerar_grafico3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', grafico1=False, grafico2=False, grafico3=False)

@app.route('/gerar_grafico')
def gerar_e_mostrar_grafico():
    gerar_grafico()  # Chama a função para gerar o gráfico 1
    return render_template('index.html', grafico1=True, grafico2=False)

@app.route('/gerar_grafico2')
def gerar_e_mostrar_grafico2():
    gerar_grafico2()  # Chama a função para gerar o gráfico 2
    return render_template('index.html', grafico1=False, grafico2=True)

@app.route('/gerar_grafico3')
def gerar_e_mostrar_grafico3():
    gerar_grafico3()  # Chama a função para gerar o gráfico 3
    return render_template('index.html', grafico1=False, grafico2=False, grafico3=True)

if __name__ == '__main__':
    app.run(debug=True)
