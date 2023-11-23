import pandas as pd
import spotipy 
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
from datetime import datetime

client_id = '4900b7eeb5f240b99c9fc4a4cb56c737'
client_secret = 'e20b8364530944a0b3b279f2235dc780'

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, 
                                                      client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

username = 'spotifycharts'
playlist_id = '5YRmjoCTiI6uPGJAevX87A'

def get_playlist_audio_features(username, playlist_id, sp):
    offset = 0
    songs = []
    ids = []
    trname = []
    artname = []
    popularity = []
    genres = []
    dates = []  # Adicionando lista para armazenar as datas
    
    while True:
        content = sp.user_playlist_tracks(username, playlist_id, fields=None, limit=100, offset=offset)
        songs += content['items']
        
        if content['next'] is not None:
            offset += 100
        else:
            break
            
    for i in songs:
        ids.append(i['track']['id'])
        trname.append(i['track']['name']) 
        artname.append(i['track']['artists'][0]['name'])
        popularity.append(i['track']['popularity'])
        
        # Obter os gêneros da primeira banda/artista (se disponíveis)
        if i['track']['artists']:
            artist_id = i['track']['artists'][0]['id']
            artist_info = sp.artist(artist_id)
            if artist_info['genres']:
                genres.append(artist_info['genres'][0])
            else:
                genres.append('N/A')
        else:
            genres.append('N/A')
        
        # Adicionar a data atual como a data de coleta das informações
        dates.append(datetime.now().strftime("%Y-%m-%d"))
        
    index = 0
    audio_features = []
    
    while index < len(ids):
        audio_features += sp.audio_features(ids[index:index + 50])
        index += 50
    
    features_list = []
    for features in audio_features:
        features_list.append([features['energy'], features['liveness'],
                              features['tempo'], features['speechiness'],
                              features['acousticness'], features['instrumentalness'],
                              features['time_signature'], features['danceability'],
                              features['key'], features['duration_ms'],
                              features['loudness'], features['valence'],
                              features['mode'], features['type'],
                              features['uri']])
    
    df = pd.DataFrame(features_list, columns=['energy', 'liveness',
                                              'tempo', 'speechiness',
                                              'acousticness', 'instrumentalness',
                                              'time_signature', 'danceability',
                                              'key', 'duration_ms', 'loudness',
                                              'valence', 'mode', 'type', 'uri'])
    
    df['name_artist'] = artname
    df['name_track'] = trname
    df['popularity'] = popularity
    df['genre'] = genres
    df['date_collected'] = dates  # Adicionando a coluna de data
    
    df.to_csv('{}-{}.csv'.format(username, playlist_id), index=False)

get_playlist_audio_features(username, playlist_id, sp)
