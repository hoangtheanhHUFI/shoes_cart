from django.db import connection

def test_raw_query():
    with connection.cursor() as cursor:
        # Define your SQL query here
        sql_query = "SELECT * FROM shoes"  # Replace 'your_table_name' with your actual table name

        # Execute the query
        cursor.execute(sql_query)

        # Fetch the results, e.g., all rows
        results = cursor.fetchall()
    print(results)
    return results
test_raw_query()