import os
import pendulum
import pandas as pd
from airflow import DAG
from pathlib import Path
from airflow.macros import ds_add
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator


with DAG(
    'dados_climaticos',
    start_date=pendulum.datetime(2022, 8, 22, tz="UTC"),
    schedule_interval='0 0 * * 1'
) as dag:

    tarefa_1 = BashOperator(
        task_id='cria_pasta',
        bash_command='mkdir '
        f"""-p "{os.path.abspath("dados/semana_{{data_interval_end.strftime('%Y-%m-%d')}}")}"""
    )

    def extrai_dados(data_interval_end):
        city = 'Boston'
        key = 'S2288F34GLCJJ42JH4WAYS4DS'

        URL = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/' \
            f'services/timeline/{city}/{data_interval_end}/'\
            f'{ds_add(data_interval_end, 7)}?' \
            f'unitGroup=metric&include=days&key={key}&contentType=csv'

        dados = pd.read_csv(URL)

        # Criação da pasta da salvar os dados buscados pela API
        dir_data_path = os.path.abspath(
            os.path.abspath(f"dados/semana_{data_interval_end}"))
        dir_path = Path(dir_data_path)

        # salvando dados
        dados.to_csv(dir_path / 'dados_brutos.csv', index=False)
        dados[['datetime', 'tempmin', 'temp', 'tempmax']].\
            to_csv(dir_path / 'temperaturas.csv', index=False)
        dados[['datetime', 'description', 'icon']].\
            to_csv(dir_path / 'condicoes.csv', index=False)

    tarefa_2 = PythonOperator(
        task_id='extrai_dados',
        python_callable=extrai_dados,
        op_kwargs={'data_interval_end': "{{data_interval_end.strftime('%Y-%m-%d')}}"}
    )

    tarefa_1 >> tarefa_2
