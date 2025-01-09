import cx_Oracle as oracle
import os
import generateCSV as generate_csv

from donor.classes.Donor import *
from donor.classes.DonorNumber import *
from donor.classes.Address import *
from donor.classes.Contact import *
from donor.classes.Name import *
from donor.classes.Identification import *
from donor.classes.IdentChangeLog import *
from donor.queries.querySequences import query as querySequences
from donor.queries.queryProgramCodes import query as queryProgramCodes
from donor.queries.queryDonorNumberSequence import query as queryDonorNumberSequence
from donor.queries.queryIdentificationTypes import query as queryIdentificationTypes
from util.db_util import execute_query
from util.io_util import read_properties

#the function to determine the new donor details to be inserted
def new_donor(data_object, db_properties, output_path):
    # a new donor creation procedure will consist of inserts to the following tables:
    #   * dnr$donors
    #   * dnr$donor_numbers
    #   * dnr$addresses
    #   * dnr$names
    #   * dnr$contacts
    #   * dnr$identifications
    #   * dnr$ident_change_log

    # get the properties for the new donor
    properties = read_properties(os.getcwd() + '/donor/resources/newDonor.properties')

    try:
        connection = oracle.connect(db_properties['dbConnection'])
        sequences = execute_query(connection, querySequences())
        programCodes = execute_query(connection, queryProgramCodes(properties['donor.programCode']))
        donorNumberSequence = execute_query(connection, queryDonorNumberSequence())
        primary = execute_query(connection, queryIdentificationTypes(properties['primary.identificationType']))
        secondary = execute_query(connection, queryIdentificationTypes(properties['secondary.identificationType']))

    except oracle.DatabaseError as error:
        print("Database Error: ", error)

    finally:
        if connection:
            connection.close()

    # set ids, update properties as necessary
    donor_id = sequences['DONORS']
    donor_number_id = sequences['DONOR_NUMBERS']
    address_id = sequences['ADDRESSES']
    contact_id = sequences['CONTACTS']
    name_id = sequences['NAMES']

    primary_identification_id = sequences['IDENTIFICATIONS']
    secondary_identification_id = primary_identification_id + 1

    primary_ident_change_log_id = sequences['IDENT_CHANGE_LOG']
    secondary_ident_change_log_id = primary_ident_change_log_id + 1

    properties['donor.programCode'] = programCodes['ID']
    properties['donor.donorNumber'] = str(donorNumberSequence['NEXT_NUM'])
    properties['primary.identificationType'] = primary['ID']
    properties['secondary.identificationType'] = secondary['ID']


    donor = build_donor(donor_id, donor_number_id, address_id, name_id, properties, output_path)
    donor_number = build_donor_number(donor_number_id, donor_id, properties, output_path)
    address = build_donor_address(address_id, donor_id, properties, output_path)
    contact = build_donor_contact(contact_id, donor_id, properties, output_path)
    name = build_donor_name(name_id, donor_id, properties, output_path)
    identifications = build_donor_identifications(
        primary_identification_id,
        secondary_identification_id,
        primary_ident_change_log_id,
        secondary_ident_change_log_id,
        donor_id,
        properties,
        output_path)

    return update_data_object(data_object, donor, donor_number, name)

# build the donor and export the .csv
def build_donor(
        id,
        donor_number_id,
        address_id,
        name_id,
        dictionary,
        output_path):
    donor = Donor(id, donor_number_id, address_id, name_id, dictionary)
    generate_csv.export(Donor.csv_header(), [donor.csv_row()], output_path + Donor.export_path())
    return donor

# build the donor number and export the .csv
def build_donor_number(
        id,
        donor_id,
        dictionary,
        output_path):
    #
    donor_number = DonorNumber(id, donor_id, dictionary)
    generate_csv.export(DonorNumber.csv_header(), [donor_number.csv_row()], output_path + DonorNumber.export_path())
    return donor_number

def build_donor_address(
        id,
        donor_id,
        dictionary,
        output_path):
    #
    address = Address(id, donor_id, dictionary)
    generate_csv.export(Address.csv_header(), [address.csv_row()], output_path + Address.export_path())
    return address

def build_donor_contact(
        id,
        donor_id,
        dictionary,
        output_path):
    #
    contact = Contact(id, donor_id, dictionary)
    generate_csv.export(Contact.csv_header(), [contact.csv_row()], output_path + Contact.export_path())
    return contact

def build_donor_name(
        id,
        donor_id,
        dictionary,
        output_path):
    #
    name = Name(id, donor_id, dictionary)
    generate_csv.export(Name.csv_header(), [name.csv_row()], output_path + Name.export_path())
    return name

def build_donor_identifications(
        primary_identification_id,
        secondary_identification_id,
        primary_ident_change_log_id,
        secondary_ident_change_log_id,
        donor_id,
        dictionary,
        output_path):
    #
    primary_identification = Identification(primary_identification_id, donor_id, dictionary, 'PRIMARY')
    secondary_identification = Identification(secondary_identification_id, donor_id, dictionary, 'SECONDARY')
    generate_csv.export(
        Identification.csv_header(),
        [primary_identification.csv_row(), secondary_identification.csv_row()],
        output_path + Identification.export_path())

    primary_ident_change_log = IdentChangeLog(primary_ident_change_log_id, primary_identification, dictionary)
    secondary_ident_change_log = IdentChangeLog(secondary_ident_change_log_id, secondary_identification, dictionary)
    generate_csv.export(
        IdentChangeLog.csv_header(),
        [primary_ident_change_log.csv_row(), secondary_ident_change_log.csv_row()],
        output_path + IdentChangeLog.export_path())
    return {
        'PRIMARY_IDENTIFICATION':primary_identification,
        'SECONDARY_IDENTIFICATION':secondary_identification,
        'PRIMARY_IDENT_CHANGE_LOG':primary_ident_change_log,
        'SECONDARY_IDENT_CHANGE_LOG':secondary_ident_change_log
    }

# update the data_object
def update_data_object(
        data_object,
        donor,
        donor_number,
        name):
    #
    data_object.site_id = donor.site_id
    data_object.donor_id = donor.id
    data_object.donor_birth_date = donor.birth_date
    data_object.donor_gender_ind = donor.gender_ind
    data_object.donor_language_ind = donor.language_ind
    data_object.donor_program_code_id = donor.program_id
    data_object.donor_collection_type_code = donor.collection_type_code
    data_object.donor_number = donor_number.donor_number
    data_object.first_name = name.name_first
    data_object.last_name = name.name_last
    return data_object