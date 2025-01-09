# returns the query for selecting a DNR$REVIEW_TYPES record with the matching 'code'
def query(code):
    return "SELECT * FROM dnr$review_types x WHERE x.code = '" + code + "'"