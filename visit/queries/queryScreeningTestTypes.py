# returns the query for selecting a DNR$SCREENING_TEST_TYPES record with the matching 'code'
def query(code):
    return "SELECT * FROM dnr$screening_test_types x WHERE x.code = '" + code + "'"