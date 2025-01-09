# returns the query for selecting a DNR$CONSENT_TYPES record with the matching 'code'
def query(donorNumber):
    return "SELECT * FROM dnr$donors x WHERE x.donrnum_id = (SELECT y.donor_id FROM dnr$donor_numbers y WHERE y = '" + donorNumber + "')"