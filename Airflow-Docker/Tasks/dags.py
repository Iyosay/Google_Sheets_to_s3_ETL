from airflow import DAG
from airflow.operators.python import PythonOperator
from Tasks.Google_sheet import extract_records

default_args = {
'owner': 'joy',
'retries': 1
}

dag = DAG(
dag_id = "joy_DE_bio_data",
description = "Extract data from googlesheet and store to s3",
default_args = default_args
)

googlesheet_to_s3 = PythonOperator(
task_id = "googlesheet_to_s3",
dag = dag,
python_callable = extract_records
)

googlesheet_to_s3
