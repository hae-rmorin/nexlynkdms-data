# returns the query for selecting the next sequnces for the appropriate tables when creating a new visit record
def query(prefix):
    return "SELECT * FROM col$collection_sequence x WHERE x.prefix_site_id = '" + prefix + "'"