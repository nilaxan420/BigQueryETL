# This script is used to connect to BigQuery
# using the Python client library.

from google.cloud import bigquery

print("hello")

# Construct a BigQuery client object.
client = bigquery.Client.from_service_account_json(
    "../bigqueryetl-387220-a3a83647ba1c.json"
)


# If the connection is successful, print a success message.
print("Connected to BigQuery successfully!")
