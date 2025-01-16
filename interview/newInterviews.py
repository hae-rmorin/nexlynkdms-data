import cx_Oracle as oracle
import os
import generateCSV as generate_csv

from interview.queries.querySequences import query as query_sequences
from interview.queries.queryProfileInterviewTypes import query as query_profile_interview_types

from util.db_util import *
from util.io_util import read_properties

def new_interviews(data_object, db_properties, output_path):

    # get the properties for the new interviews
    dictionary = read_properties(os.getcwd() + '/interview/resources/newInterviews.properties')

    try:
        connection = oracle.connect(db_properties['dbConnection'])
        sequences = execute_query(connection, query_sequences())



    except oracle.DatabaseError as error:
        print("Database Error: ", error)

    finally:
        if connection:
            connection.close()

#def new_interview():
