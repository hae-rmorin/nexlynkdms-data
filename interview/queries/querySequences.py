# returns the query for selecting the next sequnces for the appropriate tables when creating a new visit record
def query():
    return '''SELECT * FROM (SELECT * FROM int$hpf_sequences) 
        PIVOT (MAX(next_value) FOR sequence_name IN (
            'INTERVIEWS' interviews,
            'INTV_RESPONSES' intv_responses
        ))'''