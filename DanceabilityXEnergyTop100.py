import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def gerar_grafico_danceability_energy_Top100():
    
    df = pd.read_csv('spotifycharts-5YRmjoCTiI6uPGJAevX87A.csv')

    plt.figure(figsize=(12, 6))

    cores = sns.color_palette('plasma', len(df))

    scatter = plt.scatter(df['danceability'], df['energy'], c=cores, edgecolor='black', alpha=0.7)

    plt.xlabel('Danceability', fontsize=17)
    plt.ylabel('Energy', fontsize=17)
    plt.title('Relação entre Danceability e Energy', fontsize=17)

    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)

    for i, txt in enumerate(df['name_track']):
        plt.annotate(i + 1, (df['danceability'][i], df['energy'][i]), fontsize=8, ha='right', va='bottom')

    handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=cores[i], markersize=10) for i in range(len(df))]
    plt.legend(handles, [f"{i+1}. {name}" for i, name in enumerate(df['name_track'])], title='Legenda', fontsize=10, title_fontsize=12, bbox_to_anchor=(1.05, 1), loc='upper left')

    plt.tight_layout()
    plt.savefig('static/grafico17.png', bbox_inches='tight')

    plt.close()

