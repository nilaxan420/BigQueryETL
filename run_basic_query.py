# This script runs a simple SQL query to retrieve
# the top 5 rows from the 'orders' table.

from bigquery_connect import client


def run_query(client):
    query = """
    SELECT * 
    FROM `bigqueryetl-387220.Superstore.Orders`
    LIMIT 5
    """
    query_job = client.query(query)  # Make an API request.

    results = list(query_job)

    for x in results:
        print(x)

    return results


# Call the function
results = run_query(client)
