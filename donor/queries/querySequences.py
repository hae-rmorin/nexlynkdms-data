# returns the query for selecting the next sequnces for the appropriate tables when creating a new donor record
def query():
    return '''SELECT * FROM (SELECT * FROM dnr$hpf_sequences) 
        PIVOT (MAX(next_value) FOR sequence_name IN (
            'ADDRESSES' addresses,
            'CONTACTS' contacts,
            'DONORS' donors,
            'DONOR_NUMBERS' donor_numbers,
            'IDENTIFICATIONS' identifications,
            'IDENT_CHANGE_LOG' ident_change_log,
            'NAMES' names
        ))'''