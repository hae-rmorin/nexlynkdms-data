# executes the query
def execute_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    columns = [col[0] for col in cursor.description]
    cursor.rowfactory = lambda *args: dict(zip(columns, args))
    result_set = cursor.fetchone()
    #close the cursor
    if cursor:
        cursor.close()
    return result_set

def query_all(connection, query, key):
    cursor = connection.cursor()
    cursor.execute(query)
    columns = [col[0] for col in cursor.description]
    cursor.rowfactory = lambda *args: dict(zip(columns, args))
    result_set = cursor.fetchall()
    # close the cursor
    if cursor:
        cursor.close()
    return build_dict(key, result_set)

def build_dict(key, result_set):
    d = {}
    for result in result_set:
        x = (result[key])
        d[x] = result
    return d
