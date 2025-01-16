#this query

def query():
    return '''SELECT 
    it.id AS intv_type_id,
    it.class_ind AS intv_type_class_ind,
    it.code AS intv_type_code,
    q.id AS qst_id,
    q.seq AS qst_seq,
    q.question_number AS qst_num,
    o.id AS qst_opt_id,
    o.seq AS qst_opt_seq,
    o.value AS qst_opt_value
    FROM int$interview_types it
    LEFT JOIN int$question_definitions q ON q.intvtype_id = it.id
    LEFT JOIN int$qst_options o ON o.qst_id = q.id
    WHERE it.id = 3
    AND q.gender_rule_ind = 'ALWAYS' 
    AND o.flag_for_follow_up = 0
    AND o.flag_for_deferral = 0
    AND o.flag_for_consent = 0
    AND o.flag_for_issue = 0
    AND o.flag_for_note = 0
    AND o.flag_for_physical = 0
    AND o.flag_for_qnr = 0
    AND o.flag_for_review = 0
    AND o.flag_for_sample = 0
    AND o.flag_for_medication = 0
    AND o.set_requires_attention = 0
    AND o.set_escalates_visit = 0
    ORDER BY o.id'''