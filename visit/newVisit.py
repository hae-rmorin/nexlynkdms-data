import os
import cx_Oracle as oracle
import generateCSV as generate_csv

from visit.classes.Visit import *
from visit.classes.VisitLog import *
from visit.classes.Consent import *
from visit.classes.Physical import *
from visit.classes.Questionnaire import *
from visit.classes.Review import *
from visit.classes.Sample import *
from visit.classes.ScreeningTest import *

from visit.queries.queryDonorDetails import query as query_donor_details


from visit.queries.queryCollectionSequence import query as query_collection_sequence
from visit.queries.queryConsentTypes import query as query_consent_types
from visit.queries.queryQuestionnaireTypes import query as query_questionnaire_types
from visit.queries.queryPhysicalTypes import query as query_physical_types
from visit.queries.queryReviewTypes import query as query_review_types
from visit.queries.querySampleTypes import query as query_sample_types
from visit.queries.queryScreeningTestTypes import query as query_screening_test_types
from visit.queries.querySequences import query as query_sequences
from visit.queries.queryVisitPlans import query as query_visit_plans

from util.db_util import *
from util.io_util import read_properties
from util.visit_util import *

#this function will create the required .csv files for creation of a new visit
def new_visit(data_object, db_properties, output_path):
    # get the properties for the new visit
    dictionary = read_properties(os.getcwd() + '/visit/resources/newVisit.properties')

    try:
        connection = oracle.connect(db_properties['dbConnection'])

        sequences = execute_query(connection, query_sequences())
        collection_sequence = execute_query(connection, query_collection_sequence(dictionary['visit.siteId']))

        consent_types = query_all(connection, query_consent_types(), 'CODE')
        physical_types = query_all(connection, query_physical_types(), 'CODE')
        questionnaire_types = query_all(connection, query_questionnaire_types(), 'CODE')
        review_types = query_all(connection, query_review_types(), 'CODE')
        sample_types = query_all(connection, query_sample_types(), 'CODE')
        screening_test_types = query_all(connection, query_screening_test_types(), 'CODE')
        visit_plans = query_all(connection, query_visit_plans(data_object.donor_program_code_id), 'VISIT_TYPE_CODE')

    except oracle.DatabaseError as error:
        print("Database Error: ", error)

    finally:
        if connection:
            connection.close()

    #update dictionary as necessary
    visit_id = sequences['VISITS'] if sequences['VISITS'] is not None else 1
    consent_id = sequences['CONSENTS'] if sequences['CONSENTS'] is not None else 1
    physical_id = sequences['PHYSICALS'] if sequences['PHYSICALS'] is not None else 1
    questionnaire_id = sequences['QUESTIONNAIRES'] if sequences['QUESTIONNAIRES'] is not None else 1
    review_id = sequences['REVIEWS'] if sequences['REVIEWS'] is not None else 1
    sample_id = sequences['SAMPLES'] if sequences['SAMPLES'] is not None else 1
    screening_test_id = sequences['SCREENING_TESTS'] if sequences ['SCREENING_TESTS'] is not None else 1

    dictionary['visit.id'] = visit_id
    dictionary['visit.donorId'] = data_object.donor_id
    dictionary['visit.programId'] = data_object.donor_program_id
    dictionary['visit.collectionTypeCode'] = data_object.donor_collection_type_code
    dictionary['visit.collectionNumber'] = collection_sequence['PREFIX_SITE_ID'] + str(int(collection_sequence['LAST_SEQUENCE']) + 1).zfill(7)

    dictionary['review.reviewTypeId.cdcs'] = review_types[dictionary['reviewType.code.cdcs']]['ID']
    dictionary['review.reviewTypeId.nddr'] = review_types[dictionary['reviewType.code.nddr']]['ID']
    dictionary['review.reviewTypeId.addr'] = review_types[dictionary['reviewType.code.addr']]['ID']

    dictionary['screeningTest.screeningTestId.bp-sys'] = screening_test_types[dictionary['screeningTestType.code.bp-sys']]['ID']
    dictionary['screeningTest.screeningTestId.bp-dia'] = screening_test_types[dictionary['screeningTestType.code.bp-dia']]['ID']
    dictionary['screeningTest.screeningTestId.pulse'] = screening_test_types[dictionary['screeningTestType.code.pulse']]['ID']
    dictionary['screeningTest.screeningTestId.temp'] = screening_test_types[dictionary['screeningTestType.code.temp']]['ID']
    dictionary['screeningTest.screeningTestId.hct'] = screening_test_types[dictionary['screeningTestType.code.hct']]['ID']
    dictionary['screeningTest.screeningTestId.tp'] = screening_test_types[dictionary['screeningTestType.code.tp']]['ID']
    dictionary['screeningTest.screeningTestId.height'] = screening_test_types[dictionary['screeningTestType.code.height']]['ID']
    dictionary['screeningTest.screeningTestId.weight'] = screening_test_types[dictionary['screeningTestType.code.weight']]['ID']

    if data_object.new_donor:
        #print("NEW DONOR")
        dictionary['visit.visitNumber'] = visit_number(data_object.donor_number, None)

        visit_plan = visit_plans[dictionary['visit.visitType.donationPhysical']]
        dictionary['visit.visitTypeId'] = visit_plan['VISIT_TYPE_ID']
        dictionary['visit.screeningFormId'] = visit_plan['DONOR_SUITABILITY_RULESET_ID']
        dictionary['visit.donorSuitabilityRulesetId'] = visit_plan['DONOR_SUITABILITY_RULESET_ID']

        dictionary['visit.pptaReportClassInd'] = 'A1'

        dictionary['consent.consentTypeId'] = consent_types[dictionary['consentType.code.plasmaphereis']]['ID']
        dictionary['physical.physicalTypeId'] = physical_types[dictionary['physicalType.code.physical']]['ID']
        dictionary['questionnaire.questionnaireTypeId'] = questionnaire_types[dictionary['questionnaireType.code.fdhq']]['ID']

        dictionary['sample.sampleTypeId.aby'] = sample_types[dictionary['sampleType.code.aby']]['ID']
        dictionary['sample.sampleTypeId.serum'] = sample_types[dictionary['sampleType.code.serum']]['ID']

        # to pass to the data_object
        cons = dictionary['consentType.code.plasmaphereis']
        phys = dictionary['physicalType.code.physical']
        qnr = dictionary['questionnaireType.code.fdhq']

    else:
        print("EXISTING DONOR")

        cons = None
        phys = None
        qnr = dictionary['questionnaireType.code.adhq']

    # do the work
    visit = build_visit(visit_id, dictionary, output_path)
    visit_log = build_visit_log(dictionary, output_path)
    consent = build_consent(consent_id, dictionary, output_path)
    physical = build_physical(physical_id, dictionary, output_path)
    questionnaire = build_questionnaire(questionnaire_id, dictionary, output_path)
    reviews = build_reviews(review_id, dictionary, output_path)
    samples = build_samples(sample_id, dictionary, output_path)
    screening_tests = build_screening_tests(screening_test_id, dictionary, output_path)

    return update_data_object(data_object, visit, [cons], [qnr], [phys])


def build_visit(id, dictionary, output_path):
    visit = Visit(id, dictionary)
    generate_csv.export(Visit.csv_header(), [visit.csv_row()], output_path + Visit.export_path())
    return visit

def build_visit_log(dictionary, output_path):
    visit_log = VisitLog(dictionary)
    generate_csv.export(VisitLog.csv_header(), [visit_log.csv_row()], output_path + VisitLog.export_path())
    return visit_log

def build_consent(id, dictionary, output_path):
    consent = Consent(id, dictionary)
    generate_csv.export(Consent.csv_header(), [consent.csv_row()], output_path + Consent.export_path())
    return consent

def build_physical(id, dictionary, output_path):
    physical = Physical(id, dictionary)
    generate_csv.export(Physical.csv_header(), [physical.csv_row()], output_path + Physical.export_path())
    return physical

def build_questionnaire(id, dictionary, output_path):
    questionnaire = Questionnaire(id, dictionary)
    generate_csv.export(Questionnaire.csv_header(), [questionnaire.csv_row()], output_path + Questionnaire.export_path())
    return questionnaire

def build_review(id, review_type_id, ref_number, dictionary):
    review = Review(id, review_type_id, ref_number, dictionary)
    return review

def build_reviews(id, dictionary, output_path):
    cdcs = build_review(id, dictionary['review.reviewTypeId.cdcs'], 'REF_TEST_CDCS', dictionary)
    nddr = build_review(int(id) + 1, dictionary['review.reviewTypeId.nddr'], 'REF_TEST_NDDR', dictionary)
    addr = build_review(int(id) + 2, dictionary['review.reviewTypeId.addr'], None, dictionary)

    reviews = [cdcs.csv_row(), nddr.csv_row(), addr.csv_row()]
    generate_csv.export(Review.csv_header(), reviews, output_path + Review.export_path())
    return reviews

def build_sample(id, sample_type_id, dictionary):
    sample = Sample(id, sample_type_id, dictionary)
    return sample

def build_samples(id, dictionary, output_path):
    aby = build_sample(id, dictionary['sample.sampleTypeId.aby'], dictionary)
    serum = build_sample(int(id) + 1, dictionary['sample.sampleTypeId.serum'], dictionary)

    samples = [aby.csv_row(), serum.csv_row()]
    generate_csv.export(Sample.csv_header(), samples, output_path + Sample.export_path())
    return samples

def build_screening_test(id, screening_test_type_id, result, dictionary):
    screening_test = ScreeningTest(id, screening_test_type_id, result, dictionary)
    return screening_test

def build_screening_tests(id, dictionary, output_path):
    bp_sys = ScreeningTest(id, dictionary['screeningTest.screeningTestId.bp-sys'], random_bp_sys(), dictionary)
    bp_dia = ScreeningTest(int(id) + 1, dictionary['screeningTest.screeningTestId.bp-dia'], random_bp_dia(), dictionary)
    pulse = ScreeningTest(int(id) + 2, dictionary['screeningTest.screeningTestId.pulse'], random_pulse(), dictionary)
    temp = ScreeningTest(int(id) + 3, dictionary['screeningTest.screeningTestId.temp'], random_temp(), dictionary)
    hct = ScreeningTest(int(id) + 4, dictionary['screeningTest.screeningTestId.hct'], random_hct(), dictionary)
    tp = ScreeningTest(int(id) + 5, dictionary['screeningTest.screeningTestId.tp'], random_tp(), dictionary)
    height = ScreeningTest(int(id) + 6, dictionary['screeningTest.screeningTestId.height'], random_height(), dictionary)
    weight = ScreeningTest(int(id) + 7, dictionary['screeningTest.screeningTestId.weight'], random_weight(), dictionary)

    screening_tests = [
        bp_sys.csv_row(),
        bp_dia.csv_row(),
        pulse.csv_row(),
        temp.csv_row(),
        hct.csv_row(),
        tp.csv_row(),
        height.csv_row(),
        weight.csv_row()]
    generate_csv.export(ScreeningTest.csv_header(), screening_tests, output_path + ScreeningTest.export_path())
    return screening_tests

def update_data_object(data_object, visit, consents, questionnaires, physicals):
    data_object.visit_id = visit.id
    data_object.visit_number = visit.visit_number
    data_object.collection_number = visit.collection_number

    data_object.consent = consents[0]
    data_object.questionnaires = questionnaires[0]
    data_object.physicals = physicals[0]

    return data_object