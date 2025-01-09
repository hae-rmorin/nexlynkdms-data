# returns the query for selecting a DNR$CONSENT_TYPES record with the matching 'code'
def query():
    return "SELECT * FROM dnr$consent_types x"