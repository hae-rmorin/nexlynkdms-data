# returns the query for selecting a DNR$SAMPLE_TYPES record with the matching 'code'
def query():
    return "SELECT * FROM dnr$sample_types x"