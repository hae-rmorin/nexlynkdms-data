# returns the query for selecting a DNR$QUESTIONNAIRE_TYPES record with the matching 'code'
def query(code):
    return "SELECT * FROM dnr$questionnaire_types x WHERE x.code = '" + code + "'"