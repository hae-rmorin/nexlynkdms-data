#main program file

import os
import sys
import cx_Oracle as oracle

#from collection.collection import new_collection

#from interview.interviews import new_interviews
#from interview.interviews import new_interviews

from classes.DataObject import *
from donor.newDonor import new_donor
from visit.newVisit import new_visit
from util.io_util import read_properties

#intialize the oracle instant client
oracle.init_oracle_client(lib_dir = os.getcwd() + '/_OracleInstantClient')

output_path = "C:/Users/RMORIN/Desktop/sqlldr"
db_properties = read_properties(os.getcwd() + '/resources/database.properties')

data_object = DataObject()
data_object.new_donor = True

#create the new donor and associated records
data_object = new_donor(data_object, db_properties, output_path)

#create the new visit and associated records
data_object = new_visit(data_object, db_properties, output_path)


print(data_object.visit_number)

#create the new interview(s) and associated records
#new_interviews(data_object, True, True, True, False, path)

#crete the new collection and associated records
#new_collection(data_object, True, path)