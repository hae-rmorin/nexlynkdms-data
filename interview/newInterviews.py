import cx_Oracle as oracle
import os
import generateCSV as generate_csv

from interview.queries.querySequences import query as query_sequences
from interview.queries.queryProfileInterviewTypes import query as query_profile_interview_types
from interview.queries.queryInterviewResponses import query as query_interview_responses

from util.db_util import *
from util.io_util import read_properties

def new_interviews(data_object, db_properties, output_path):

    site_id = data_object.site_id

    # get the properties for the new interviews
    dictionary = read_properties(os.getcwd() + '/interview/resources/newInterviews.properties')

    try:
        connection = oracle.connect(db_properties['dbConnection'])
        sequences = execute_query(connection, query_sequences())

        #TODO: consider refactoring to handle the potential scenario where there are duplicates, ie: if there is a consent/question with the same name
        profile_interview_types = query_all(connection, query_profile_interview_types(site_id), 'ACTIVITY_TYPE_CODE')
        #DEBUG#print(profile_interview_types)

        #determine which interviews to create
        consent = data_object.consent
        questionnaire = data_object.questionnaire
        physical = data_object.physical

        consent_response_details = None
        physical_response_details = None
        questionnaire_response_details = None
        if consent is not None:
            consent_response_details = query_all(connection, query_interview_responses(), 'QST_NUM')
        if physical is not None:
            physical_response_details = query_all(connection, query_interview_responses(), 'QST_NUM')
        if questionnaire is not None:
            questionnaire_response_details = query_all(connection, query_interview_responses(), 'QST_NUM')



    except oracle.DatabaseError as error:
        print("Database Error: ", error)

    finally:
        if connection:
            connection.close()

    #build consent interview details
    #build physical interview details
    #build questionnaire interview details

    return data_object

def build_interview(id, dictionary):
    interview = Interview(id, dictionary)
    print("inside build_interview()")
    generate_csv.export(Interview.csv_header(), [interview.csv_row()], output_path + Interview.export_path())
    return interview

def build_interview_log(interview, dictionary):
    interview_log = InterviewLog(interview, dictionary)
    return interview_log

def build_interview_response(interview, question_id, dictionary):
    interview_response = InterviewResponse(interview, question_id, dictionary)
    return interview_response

def build_interview_response_value(interview_response_id, question_id, dictionary):
    interview_response_value = InterviewResponseValue(interview_response_id, question_option_id)
    return interview_response_value

def build_interview_response_log():
    interview_response_log = None
    return interview_response_log
