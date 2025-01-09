#Consent
from visit.classes.Activity import Activity

class Questionnaire(Activity):
    def __init__(self, id, donor_id, visit_id, dictionary):
        super().__init__(id, donor_id, visit_id)
        self.questionnaire_type_id = dictionary['']

@staticmethod
    def export_path():
        return '/visit/dnr$questionnaires/questionnaires.csv'

    @staticmethod
    def csv_header():
        return [
            '#dnr$questionnaires.id',
            '#dnr$questionnaires.version',
            '#dnr$questionnaires.donor_id',
            '#dnr$questionnaires.visit_id',
            '#dnr$questionnaires.qnrtype_id',
            '#dnr$questionnaires.schedule_reason',
            '#dnr$questionnaires.result_value',
            '#dnr$questionnaires.result_assess_ind',
            '#dnr$questionnaires.result_ts',
            '#dnr$questionnaires.created_in_tz',
            '#dnr$questionnaires.is_legacy',
            '#dnr$questionnaires.actions_taken_flag',
            '#dnr$questionnaires.escalated_visit',
            '#dnr$questionnaires.is_external'
        ]

    def csv_row(self):
        return {
            '#dnr$questionnaires.id':self.id,
            '#dnr$questionnaires.version':self.version,
            '#dnr$questionnaires.donor_id':self.donor_id,
            '#dnr$questionnaires.visit_id':self.visit_id,
            '#dnr$questionnaires.qnrtype_id':self.questionnaire_type_id,
            '#dnr$questionnaires.schedule_reason':self.schedule_reason,
            '#dnr$questionnaires.result_value':self.result_value,
            '#dnr$questionnaires.result_assess_ind':self.result_assessment_ind,
            '#dnr$questionnaires.result_ts':self.result_ts,
            '#dnr$questionnaires.created_in_tz':self.created_in_tz,
            '#dnr$questionnaires.is_legacy':self.is_legacy,
            '#dnr$questionnaires.actions_taken_flag':self.actions_taken_flag,
            '#dnr$questionnaires.escalated_visit':self.escalated_visit,
            '#dnr$questionnaires.is_external':self.is_external
        }