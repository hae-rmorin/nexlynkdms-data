# returns the query for selecting the next sequence from the DNR$DONOR_NUMBERS_SEQUENCE table
def query():
    return "SELECT x.next_num FROM dnr$donor_number_sequence x"