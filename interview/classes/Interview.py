from classes.Record import *

#Interview
class Interview(Record):
    def __init__(self, id, dictionary):
        super().__init__(id)
        self.interview_type_id = None
        self.activity_type_code = None
        self.interview_date = None
        self.donor_number = None
        self.visit_number = None
        self.site_id = None
        self.first_name = None
        self.last_name = None
        self.language_ind = None
        self.gender_ind = None
        self.status_ind = None
        self.escalated_visit = 0

    @staticmethod
    def export_path():
        return '/interview/int$interviews/interviews.csv'

    @staticmethod
    def csv_header():
        return [
            '#int$interview.id',
            '#int$interview.version',
            '#int$interview.intvtype_id',
            '#int$interview.acttype_code',
            '#int$interview.intv_date',
            '#int$interview.donor_number',
            '#int$interview.visit_number',
            '#int$interview.site_id',
            '#int$interview.first_name',
            '#int$interview.last_name',
            '#int$interview.language_ind',
            '#int$interview.gender_ind',
            '#int$interview.status_ind',
            '#int$interview.escalated_visit'
        ]

    def csv_row(self):
        return {
            '#int$interview.id':self.id,
            '#int$interview.version':self.version,
            '#int$interview.intvtype_id':self.interview_type_id,
            '#int$interview.acttype_code':self.activity_type_code,
            '#int$interview.intv_date':self.interview_date,
            '#int$interview.donor_number':self.donor_number,
            '#int$interview.visit_number':self.visit_number,
            '#int$interview.site_id':self.site_id,
            '#int$interview.first_name':self.first_name,
            '#int$interview.last_name':self.last_name,
            '#int$interview.language_ind':self.language_ind,
            '#int$interview.gender_ind':self.gender_ind,
            '#int$interview.status_ind':self.status_ind,
            '#int$interview.escalated_visit':self.escalated_visit
        }