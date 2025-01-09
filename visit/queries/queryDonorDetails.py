# returns the query for selecting donor details (and most recent visit record)
def query(donorNumber):
    return '''
        SELECT
            d.id AS donor_id,
            dn.donor_number as donor_number,
            n.name_last as donor_last_name,
            n.name_first as donor_first_name,
            d.birth_date as donor_birth_date,
            d.gender_ind as donor_gender_ind,
            d.lang_ind as donor_lang_ind,
            d.program_code_id as donor_program_id,
            d.collection_type_code as donor_collection_type_code,
            v.id as visit_id,
            v.visit_number as visit_number,
            v.vsttype_id as visit_type_id,
            v.visit_date as visit_date,
            v.coll_number as collection_number,
            d.site_id as site_id,
            t.java_id as site_timezone
        FROM dnr$donors d
        JOIN dnr$donor_numbers dn ON dn.id = d.donrnum_id
        JOIN dnr$names n ON n.id = d.donrname_id
        LEFT JOIN dnr$visits v ON v.donor_id = d.id
        JOIN svc$sites s ON s.code = d.site_id
        JOIN svc$timezones t ON t.id = s.timezone_id
        WHERE v.visit_date = (SELECT MAX(visit_date) FROM DNR$VISITS WHERE donor_id = d.id)
        AND dn.donor_number = ''' + "'" + donorNumber + "'"
        
