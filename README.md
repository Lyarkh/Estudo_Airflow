# Estudos Formação Airflow

![last commit](https://img.shields.io/github/last-commit/Lyarkh/Estudo_Airflow)
![python version](https://img.shields.io/badge/python-3.9%20%7C%203.10-green)

Repositório onde se encontrará estudos da ferramenta apache Airflow.

- Criação e monitoramento de Pipelines.
- Criação de DAGs.
- Entendimento de ETL utilizando python.

## Principais conceitos do Airflow

O Airflow organiza fluxos de trabalho em DAGs, que são basicamente pipelines de addos definidos utilizando a linguagem python.

- **DAG**: fluxo de trabalho definido em python.
- **TAsk**: unidade mais básica de uma *DAG*
- **Operator**: encapsula a lógica para fazer uma unidade de trabalho (task)

## Principais componentes da arquitetura do Airflow

- **Webserver**: apresenta uma interface de usuário que nos permite inspecionar, acionar e acompanhar o comportamento dos DAGs e suas tarefas
- **Pasta de arquivos DAG**: armazena os arquivos DAGs criados
- **Scheduler**: lida com o acionamento dos fluxos de travalh(agendador)
- **Banco de dados**: usado pelo agendador, executor e webserver para armazenar os metadados e status do DAG e suas tarefas
- **Executor**: lida com as tarefas em execução. o Airflow possui vários executores, mais apenas um é utilizado por vez

## Criando ambiente virtual e ativando

`PowerShell`:

```bash
  python -m venv venv
  venv/Scripts/Activate.ps1
```

`Bash`:

```bash
  python3 -m venv venv
  source venv/bin/activate
```
