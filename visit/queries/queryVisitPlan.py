#
def query(program_id, visit_type_code):
    return "SELECT * FROM dnr$visit_plan_matrix v WHERE v.program_id = " + str(program_id) + " AND v.vsttype_id = (SELECT vt.id FROM dnr$visit_type_codes vt WHERE vt.code = '" + visit_type_code + "')"