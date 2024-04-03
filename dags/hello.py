from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    "owner": "the-ape-labs",
    "start_date": datetime(year=2024, month=4, day=3),
    "catchup": False
}

dag = DAG(
    dag_id= "hello_world",
    default_args= default_args,
    schedule= timedelta(days=1)
)

# Define the tasks 
t1 = BashOperator(
    task_id= "hello_world",
    bash_command='echo "hello world"',
    dag= dag
)
 
t2 = BashOperator(
    task_id= "hello_tal",
    bash_command='echo "hello the-ape-labs"',
    dag= dag
)
