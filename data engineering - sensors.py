from airflow.exceptions import AirflowException
from airflow import models
from airflow import DAG
from datetime import datetime, timedelta
from airflow.utils.email import send_email
from dateutil.relativedelta import relativedelta
import os

#please fill in the values required
#interval of the dag run
# datetime.timedelta(days=1)
# '0 2 1 * *' ' min hour dayofmonth month dayofweek'
schedule_interval_dag = timedelta(days=1)

default_dag_args = {
    # Setting start date as yesterday starts the DAG immediately when it is
    # detected in the Cloud Storage bucket.
    # set your start_date : airflow will run previous dags if dags since startdate has not run
    'start_date': '2019-08-30',
    'email_on_failure': True,
    'email_on_retry': True,
    'project_id' : 'your project id',
    'retries': 1,
    'on_failure_callback': notify_email,
    'retry_delay': timedelta(minutes=5),
}

with models.DAG(
    dag_id='dag name',
    # Continue to run DAG once per day
    schedule_interval = schedule_interval_dag,
    catchup = True,
    default_args=default_dag_args) as dag:

    check_data_source_1 =
        ExternalSensor.ExternalTaskSensor(
        task_id='check_data_source_1',
        external_dag_id='dag of data source 1',
        external_task_id= 'last task of the dag',
        execution_delta = timedelta(hours=1),
        timeout = 300)

    check_data_source_2 =
        ExternalSensor.ExternalTaskSensor(
        task_id='check_data_source_2',
        external_dag_id='dag of data source 2',
        external_task_id= 'last task of the dag',
        execution_delta = timedelta(hours=1),
        timeout = 300)

    check_external_data_source_1 =
        ExternalSensor.ExternalTaskSensor(
        task_id='check_external_data_source_1',
        external_dag_id='dag of external data source 1',
        external_task_id= 'last task of the dag',
        execution_delta = timedelta(hours=1),
        timeout = 300)

    check_external_data_source_2 =
        ExternalSensor.ExternalTaskSensor(
        task_id='check_external_data_source_2',
        external_dag_id='dag of external data source 2',
        external_task_id= 'last task of the dag',
        execution_delta = timedelta(hours=1),
        timeout = 300)

    transform_table_1 = 
        # code for transfromation of table 1

    check_data_source_1
    check_data_source_2
    check_external_data_source_1
    check_external_data_source_2
    transform_table_1.set_upstream([check_data_source_1,check_data_source_2,check_external_data_source_1,check_external_data_source_2])





