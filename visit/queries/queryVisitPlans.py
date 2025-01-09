#
def query(program_id):
    return '''
        SELECT 
            vp.id AS visit_plan_id,
            vp.program_id AS program_id,
            vt.id AS visit_type_id,
            vt.code AS visit_type_code,
            vp.dnrsuit_id AS donor_suitability_ruleset_id,
            vp.scrnform_id as screening_form_id
        FROM dnr$visit_plan_matrix vp 
        JOIN dnr$visit_type_codes vt ON vt.id = vp.vsttype_id
        WHERE vp.program_id = ''' + str(program_id)