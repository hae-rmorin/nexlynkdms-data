import os
import cx_Oracle as oracle
import generateCSV as generate_csv


from visit.classes.Visit import *
#from visit.queries.queryDonors import query as query_donors

from visit.queries.queryCollectionSequence import query as query_collection_sequence
from visit.queries.queryConsentTypes import query as query_consent_type
from visit.queries.queryQuestionnaireTypes import query as query_questionnaire_type
from visit.queries.queryPhysicalTypes import query as query_physical_type
from visit.queries.queryReviewTypes import query as query_review_type
from visit.queries.querySampleTypes import query as query_sample_type
from visit.queries.queryScreeningTestTypes import query as query_screening_test_type
from visit.queries.querySequences import query as query_sequences
from visit.queries.queryVisitPlan import query as query_visit_plan

from util.db_util import execute_query
from util.io_util import read_properties

#this function will create the required .csv files for creation of a new visit
def new_visit(data_object, db_properties, output_path):

    # get the properties for the new visit
    properties = read_properties(os.getcwd() + '/visit/resources/newVisit.properties')

    try:
        connection = oracle.connect(db_properties['dbConnection'])

        sequences = execute_query(connection, query_sequences())
        consent_type = execute_query(connection, query_consent_type(properties['consentType.code.plasmaphereis']))
        physical_type = execute_query(connection, query_physical_type(properties['physicalType.code.physical']))
        fdhq_questionnaire_type = execute_query(connection, query_questionnaire_type(properties['questionnaireType.code.fdhq']))
        adhq_questionnaire_type = execute_query(connection, query_questionnaire_type(properties['questionnaireType.code.adhq']))
        cdcs_review_type = execute_query(connection, query_review_type(properties['reviewType.code.cdcs']))
        nddr_review_type = execute_query(connection, query_review_type(properties['reviewType.code.nddr']))
        addr_review_type = execute_query(connection, query_review_type(properties['reviewType.code.addr']))
        bp_sys_screening_test_type = execute_query(connection, query_screening_test_type(properties['screeningTestType.code.bp-sys']))
        bp_dia_screening_test_type = execute_query(connection, query_screening_test_type(properties['screeningTestType.code.bp-dia']))
        pulse_screening_test_type = execute_query(connection, query_screening_test_type(properties['screeningTestType.code.pulse']))
        temp_screening_test_type = execute_query(connection, query_screening_test_type(properties['screeningTestType.code.temp']))
        hct_screening_test_type = execute_query(connection, query_screening_test_type(properties['screeningTestType.code.hct']))
        tp_screening_test_type = execute_query(connection, query_screening_test_type(properties['screeningTestType.code.tp']))
        height_screening_test_type = execute_query(connection, query_screening_test_type(properties['screeningTestType.code.height']))
        weight_screening_test_type = execute_query(connection, query_screening_test_type(properties['screeningTestType.code.weight']))
        donation_visit_plan = execute_query(connection, query_visit_plan(data_object.donor_program_code_id, properties['visit.visitType.donation']))
        donation_phys_visit_plan = execute_query(connection, query_visit_plan(data_object.donor_program_code_id, properties['visit.visitType.donationPhysical']))
        collection_sequence = execute_query(connection, query_collection_sequence())

    except oracle.DatabaseError as error:
        print("Database Error: ", error)

    finally:
        if connection:
            connection.close()

    #set the ids, update properties as necessary
    visit_id = sequences['VISITS']
    consent_id = sequences['CONSENTS']
    physical_id = sequences['PHYSICALS']
    questionnaire_id = sequences['QUESTIONNAIRES']
    review_id = sequences['REVIEWS']
    sample_id = sequences['SAMPLES']
    screening_test_id = sequences['SCREENING_TESTS']

    properties['visit.donorId'] = data_object.donor_id
    properties['visit.programId'] = data_object.donor_program_id
    properties['visit.collectionTypeCode'] = data_object.donor_collection_type_code
    properties['visit.collectionNumber']



    if data_object.new_donor:
        #this means we are generating a new visit for the new donor
        #DEBUG
        print("NEW DONOR")
        # new donor will have a visit that includes the FDHQ, physical and plasmapheresis consent





    else:
        #this means we are generating a new visit for an existing donor
        #DEBUG
        print("EXISTING DONOR")
        # existing donor will have a visit that includes the ADHQ

        #set the properties
     #   properties['visit.visitTypeId'] = visit_plan['VSTTYPE_ID']
     #   properties['visit.screeningFormId'] = visit_plan['SCRNFORM_ID']
     #   properties['visit.donorSuitabilityRulesetId'] = visit_plan['DNRSUIT_ID']

        # create the new visit log



    return None

def build_visit(
        id,
        donor_id,
        dictionary,
        output_path):
    visit = Visit(id, donor_id, dictionary)
    generate_csv.export(Visit.csv_header(), [visit.csv_row()], output_path + Visit.export_path())
    return visit

def build_consent(
        id,
        donor_id,
        visit_id,
        dictionary,
        output_path):
    consent = Consent(id, donor_id, visit_id, dictionary)
    generate_csv.export(Consent.csv_header(), [consent.csv_row()], output_path + Consent.export_path())
    return consent

def build_physical(
        id,
        donor_id,
        visit_id,
        dictionary,
        output_path):
    physical = Physical(id, donor_id, visit_id, dictionary)
    generate_csv.export(Physical.csv_header(), [physical.csv_row()], output_path + Physical.export_path())
    return physical

def build_questionnaire(
        id,
        donor_id,
        visit_id,
        dictionary,
        output_path):
    questionnaire = Questionnaire(id, donor_id, visit_id, dictionary)

    return questionnaire

def build_reviews(
        id,
        donor_id,
        visit_id,
        dictionary,
        output_path):
    reviews = []
    return reviews

def build_samples(
        id,
        donor_id,
        visit_id,
        dictionary,
        output_path):
    samples = []
    return samples

def build_screening_tests(
        id,
        donor_id,
        visit_id,
        dictionary,
        output_path):
    screening_tests = []
    return screening_tests

def update_data_object():
    return None