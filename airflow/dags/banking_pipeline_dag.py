# Importa objetos principais do Airflow
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

# Define argumentos padrão da DAG
default_args = {
    "owner": "jose",
}

# Cria a DAG
with DAG(
    dag_id="banking_pipeline_dag",
    default_args=default_args,
    description="Pipeline bancario com Python, PostgreSQL e DBT",
    start_date=datetime(2026, 3, 28),
    schedule=None,  # Executa manualmente
    catchup=False,
) as dag:

    # --------------------------------------------------
    # TAREFA 1: RODAR EXTRACT + TRANSFORM
    # --------------------------------------------------
    # Executa o main.py do projeto
    run_python_pipeline = BashOperator(
        task_id="run_python_pipeline",
        bash_command="cd /opt/project && source venv/bin/activate && python main.py",
    )

    # --------------------------------------------------
    # TAREFA 2: CARREGAR DADOS NO POSTGRESQL
    # --------------------------------------------------
    # Executa o script que envia os dados para o banco
    load_to_postgres = BashOperator(
        task_id="load_to_postgres",
        bash_command="cd /opt/project && source venv/bin/activate && python scripts/load_postgres.py",
    )

    # --------------------------------------------------
    # TAREFA 3: RODAR DBT RUN
    # --------------------------------------------------
    # Executa os models do DBT
    run_dbt_models = BashOperator(
        task_id="run_dbt_models",
        bash_command="cd /opt/project/dbt_project && source ../venv/bin/activate && dbt run",
    )

    # --------------------------------------------------
    # TAREFA 4: RODAR DBT TEST
    # --------------------------------------------------
    # Executa os testes do DBT
    run_dbt_tests = BashOperator(
        task_id="run_dbt_tests",
        bash_command="cd /opt/project/dbt_project && source ../venv/bin/activate && dbt test",
    )

    # Define a ordem de execução das tarefas
    run_python_pipeline >> load_to_postgres >> run_dbt_models >> run_dbt_tests