from classes.Record import *
from util.donor_util import random_ssn, random_identification

#Identification
class Identification(Record):
    def __init__(self, id, donor_id, dictionary, indicator):
        super().__init__(id)
        self.donor_id = donor_id
        self.start_date = None
        self.valid_until_date = None
        if indicator == 'PRIMARY':
            self.identification_type_id = dictionary['primary.identificationType']
            self.identification_value = random_ssn()
            self.identification_value_unmasked = ''.join(item for item in self.identification_value if item.isalnum())
        else:
            self.identification_type_id = dictionary['secondary.identificationType']
            self.identification_value = random_identification(16)
            self.identification_value_unmasked = ''.join(item for item in self.identification_value if item.isalnum())

    @staticmethod
    def export_path():
        return '/donor/dnr$identifications/identifications.csv'

    @staticmethod
    def csv_header():
        return [
            '#dnr$identifications.id',
            '#dnr$identifications.version',
            '#dnr$identifications.donor_id',
            '#dnr$identifications.identype_id',
            '#dnr$identifications.ident_value',
            '#dnr$identifications.start_date',
            '#dnr$identifications.valid_until_date',
            '#dnr$identifications.ident_unmasked_value'
        ]

    def csv_row(self):
        return {
            '#dnr$identifications.id':self.id,
            '#dnr$identifications.version':self.version,
            '#dnr$identifications.donor_id':self.donor_id,
            '#dnr$identifications.identype_id':self.identification_type_id,
            '#dnr$identifications.ident_value':self.identification_value,
            '#dnr$identifications.start_date':self.start_date,
            '#dnr$identifications.valid_until_date':self.valid_until_date,
            '#dnr$identifications.ident_unmasked_value':self.identification_value_unmasked
        }