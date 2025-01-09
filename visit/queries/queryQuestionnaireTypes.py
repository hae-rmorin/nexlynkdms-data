# returns the query for selecting a DNR$QUESTIONNAIRE_TYPES record with the matching 'code'
def query():
    return "SELECT * FROM dnr$questionnaire_types"