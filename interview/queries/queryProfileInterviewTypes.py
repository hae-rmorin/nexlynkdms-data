def query(site_id):
    return '''SELECT 
    i.id AS profile_interview_type_id,
    i.intvtype_id AS interview_type_id,
    i.class_ind AS activity_type_class_ind,
    i.acttype_code AS activity_type_code,
    s.site_id AS site_id
    FROM int$profile_intvtypes i
    JOIN int$site_parameters s ON s.intvprof_id = i.intvprof_id
    WHERE s.site_id = ''' + "'" + site_id + "'"