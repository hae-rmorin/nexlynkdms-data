from classes.Record import *

#Contact
class Contact(Record):
    def __init__(self, id, donor_id, dictionary):
        super().__init__(id)
        self.donor_id = donor_id
        self.method_ind = 'PHONE'
        self.label_ind = 'HOME'
        self.contact_value = dictionary['contact.phone']
        self.is_preferred = 1

    @staticmethod
    def export_path():
        return '/donor/dnr$contacts/contacts.csv'

    @staticmethod
    def csv_header():
        return [
            '#dnr$contacts.id',
            '#dnr$contacts.version',
            '#dnr$contacts.donor_id',
            '#dnr$contacts.method_ind',
            '#dnr$contacts.label_ind',
            '#dnr$contacts.contact_value',
            '#dnr$contacts.is_preferred'
        ]

    def csv_row(self):
        return {
            '#dnr$contacts.id':self.id,
            '#dnr$contacts.version':self.version,
            '#dnr$contacts.donor_id':self.donor_id,
            '#dnr$contacts.method_ind':self.method_ind,
            '#dnr$contacts.label_ind':self.label_ind,
            '#dnr$contacts.contact_value':self.contact_value,
            '#dnr$contacts.is_preferred':self.is_preferred
        }