import os
import pandas as pd
from pathlib import Path
from datetime import datetime, timedelta


class ExtraiInfosClima:
    def __init__(self):
        # Parametros de data
        self.data_inicio = datetime.today()
        self.data_fim = self.data_inicio + timedelta(days=7)

        self.data_inicio = self.data_inicio.\
            strftime('%Y-%m-%d')                                # type: ignore
        self.data_fim = self.data_fim.strftime('%Y-%m-%d')      # type: ignore

    def busca_dados(self):
        # Key e cidade para busca na API
        city = 'Boston'
        key = 'S2288F34GLCJJ42JH4WAYS4DS'

        URL = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/' \
            f'services/timeline/{city}/{self.data_inicio}/{self.data_fim}?' \
            f'unitGroup=metric&include=days&key={key}&contentType=csv'

        dados = pd.read_csv(URL)

        # Criação da pasta da salvar os dados buscados pela API
        dir_data_path = os.path.abspath(
            f'01 - Primeira Pipeline/dados/semana_{self.data_inicio}')
        dir_path = Path(dir_data_path)

        # salvando dados
        dados.to_csv(dir_path / 'dados_brutos.csv', index=False)
        dados[['datetime', 'tempmin', 'temp', 'tempmax']].\
            to_csv(dir_path / 'temperaturas.csv', index=False)
        dados[['datetime', 'description', 'icon']].\
            to_csv(dir_path / 'condicoes.csv', index=False)
