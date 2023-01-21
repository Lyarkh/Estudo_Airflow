import os
import pandas as pd
from os.path import join
from datetime import datetime, timedelta


data_inicio = datetime.today()
data_fim = data_inicio + timedelta(days=7)

data_inicio = data_inicio.strftime('%Y-%m-%d')      # type: ignore
data_fim = data_fim.strftime('%Y-%m-%d')            # type: ignore


city = 'Boston'
key = 'S2288F34GLCJJ42JH4WAYS4DS'


URL = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/' \
    f'services/timeline/{city}/{data_inicio}/{data_fim}?' \
    f'unitGroup=metric&include=days?key={key}&contentType=csv'
