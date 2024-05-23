# https://python-poetry.org/docs/

# New line of code added

# https://airflow.apache.org/docs/apache-airflow/stable/installation/installing-from-pypi.html
# https://docs.dagster.io/getting-started/install

poetry add dagster dagster-webserver --find-links=https://github.com/dagster-io/build-grpcio/wiki/Wheels

poetry source add grpcio https://github.com/dagster-io/build-grpcio/wiki/Wheels


https://github.com/dagster-io/dagster/issues/15699