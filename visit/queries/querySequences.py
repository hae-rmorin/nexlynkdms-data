# returns the query for selecting the next sequnces for the appropriate tables when creating a new visit record
def query():
    return '''SELECT * FROM (SELECT * FROM dnr$hpf_sequences) 
        PIVOT (MAX(next_value) FOR sequence_name IN (
            'CONSENTS' consents,
            'PHYSICALS' physicals,
            'QUESTIONNAIRES' questionnaires,
            'REVIEWS' reviews,
            'SAMPLES' samples,
            'SCREENING_TESTS' screening_tests,
            'VISITS' visits
        ))'''