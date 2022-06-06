import time
from datetime import datetime
from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator


def test(**context):
    time.sleep(10)


default_args = {
    "owner": 'Airflow',
    "start_date": datetime(2021, 1, 1),
    "retries": 2,
}


dag = DAG(
    dag_id='dag_sleep_10s',
    schedule_interval=None,
    default_args=default_args,
    tags=["sample"],
    catchup=False,
)


with dag:
    task = PythonOperator(
        task_id="task",
        python_callable=test,
        provide_context=True
    )
