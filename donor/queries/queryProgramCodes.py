# returns the query for selecting a DNR$PROGRAM_CODES record with the matching 'code'
def query(code):
    return "SELECT * FROM dnr$program_codes x WHERE x.code = '" + code + "'"