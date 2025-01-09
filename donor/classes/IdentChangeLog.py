from classes.Record import *

#IdentChangeLog
class IdentChangeLog(Record):
    def __init__(self, id, identification, dictionary):
        super().__init__(id)
        self.donor_id = identification.donor_id
        self.identification_type_id = identification.identification_type_id
        self.identification_value = identification.identification_value
        self.identification_value_unmasked = identification.identification_value_unmasked
        self.start_date = None
        self.valid_until_date = None
        self.ident_action_ind = 'NEW_IDNT'
        self.modified_by_user_id = 'ADMIN'
        self.modification_ts = None

    @staticmethod
    def export_path():
        return '/donor/dnr$ident_change_log/ident_change_log.csv'

    @staticmethod
    def csv_header():
        return [
            '#dnr$ident_change_log.id',
            '#dnr$ident_change_log.version',
            '#dnr$ident_change_log.donor_id',
            '#dnr$ident_change_log.identype_id',
            '#dnr$ident_change_log.ident_value',
            '#dnr$ident_change_log.start_date',
            '#dnr$ident_change_log.valid_until_date',
            '#dnr$ident_change_log.ident_unmasked_value',
            '#dnr$ident_change_log.ident_action_ind',
            '#dnr$ident_change_log.modified_by_user_id',
            '#dnr$ident_change_log.modification_ts'
        ]

    def csv_row(self):
        return {
            '#dnr$ident_change_log.id':self.id,
            '#dnr$ident_change_log.version':self.version,
            '#dnr$ident_change_log.donor_id':self.donor_id,
            '#dnr$ident_change_log.identype_id':self.identification_type_id,
            '#dnr$ident_change_log.ident_value':self.identification_value,
            '#dnr$ident_change_log.start_date':self.start_date,
            '#dnr$ident_change_log.valid_until_date':self.valid_until_date,
            '#dnr$ident_change_log.ident_unmasked_value':self.identification_value_unmasked,
            '#dnr$ident_change_log.ident_action_ind':self.ident_action_ind,
            '#dnr$ident_change_log.modified_by_user_id':self.modified_by_user_id,
            '#dnr$ident_change_log.modification_ts':self.modification_ts
        }