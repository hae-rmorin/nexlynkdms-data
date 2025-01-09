# returns the query for selecting a DNR$PHYSICAL_TYPES record with the matching 'code'
def query(code):
    return "SELECT * FROM dnr$physical_types x WHERE x.code = '" + code + "'"