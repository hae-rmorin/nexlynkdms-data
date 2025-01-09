#Consent
from visit.classes.Activity import Activity

class Consent(Activity):
    def __init__(self, id, dictionary):
        super().__init__(id, dictionary)
        self.consent_type_id = dictionary['consent.consentTypeId']
        self.result_value = 'ACCEPTED'
        self.result_assessment_ind = 'OK'

    @staticmethod
    def export_path():
        return '/visit/dnr$consents/consents.csv'

    @staticmethod
    def csv_header():
        return [
            '#dnr$consents.id',
            '#dnr$consents.version',
            '#dnr$consents.donor_id',
			'#dnr$consents.visit_id',
            '#dnr$consents.constype_id',
            '#dnr$consents.schedule_reason',
            '#dnr$consents.result_value',
            '#dnr$consents.result_assess_ind',
            '#dnr$consents.result_ts',
            '#dnr$consents.created_in_tz',
            '#dnr$consents.is_legacy',
            '#dnr$consents.actions_taken_flag',
            '#dnr$consents.escalated_visit',
            '#dnr$consents.is_external'
        ]

    def csv_row(self):
        return {
            '#dnr$consents.id':self.id,
            '#dnr$consents.version':self.version,
            '#dnr$consents.donor_id':self.donor_id,
            '#dnr$consents.visit_id':self.visit_id,
            '#dnr$consents.constype_id':self.consent_type_id,
            '#dnr$consents.schedule_reason':self.schedule_reason,
            '#dnr$consents.result_value':self.result_value,
            '#dnr$consents.result_assess_ind':self.result_assessment_ind,
            '#dnr$consents.result_ts':self.result_ts,
            '#dnr$consents.created_in_tz':self.created_in_tz,
            '#dnr$consents.is_legacy':self.is_legacy,
            '#dnr$consents.actions_taken_flag':self.actions_taken_flag,
            '#dnr$consents.escalated_visit':self.escalated_visit,
            '#dnr$consents.is_external':self.is_external
        }