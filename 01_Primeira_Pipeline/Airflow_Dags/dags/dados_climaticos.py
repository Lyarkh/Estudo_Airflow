import os
import pendulum
from airflow import DAG
from airflow.operators.bash import BashOperator


with DAG(
    'dados_climaticos',
    start_date=pendulum.datetime(2022, 8, 22, tz="UTC"),
    schedule_interval='0 0 * * 1'
) as dag:

    tarefa_1 = BashOperator(
        task_id='cria_pasta',
        bash_command='mkdir '
        f"""-p "{os.path.abspath("semana_{{data_interval_end.strftime('%Y-%m-%d')}}")}"""
    )
