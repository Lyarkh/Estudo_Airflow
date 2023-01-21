import os
import pandas as pd
from pathlib import Path
from os.path import join
from datetime import datetime, timedelta


# Parametros de data
data_inicio = datetime.today()
data_fim = data_inicio + timedelta(days=7)

data_inicio = data_inicio.strftime('%Y-%m-%d')      # type: ignore
data_fim = data_fim.strftime('%Y-%m-%d')            # type: ignore

# Key e cidade para busca na API
city = 'Boston'
key = 'S2288F34GLCJJ42JH4WAYS4DS'


URL = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/' \
    f'services/timeline/{city}/{data_inicio}/{data_fim}?' \
    f'unitGroup=metric&include=days&key={key}&contentType=csv'

dados = pd.read_csv(URL)

# Criação da pasta da salvar os dados buscados pela API
dir_data_path = os.path.abspath(
    f'01 - Primeira Pipeline/dados/semana_{data_inicio}')
dir_path = Path(dir_data_path)
dir_path.mkdir(parents=True, exist_ok=True)

# salvando dados
dados.to_csv(dir_path / 'dados_brutos.csv', index=False)
dados[['datetime', 'tempmin', 'temp', 'tempmax']].\
    to_csv(dir_path / 'temperaturas.csv', index=False)
dados[['datetime', 'description', 'icon']].\
    to_csv(dir_path / 'condicoes.csv', index=False)
