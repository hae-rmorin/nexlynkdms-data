# returns the query for selecting a DNR$IDENTIFICATION_TYPES record with the matching 'code'
def query(code):
    return "SELECT * FROM dnr$identification_types x WHERE x.code = '" + code + "'"