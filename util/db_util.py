# executes the query
def execute_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    columns = [col[0] for col in cursor.description]
    cursor.rowfactory = lambda *args: dict(zip(columns, args))
    result_set = cursor.fetchone()  # there will only be a single row
    #close the cursor
    if cursor:
        cursor.close()
    return result_set