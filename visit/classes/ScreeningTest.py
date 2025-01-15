#Screening Test

class ScreeningTest:
    def __init__(self, id, screening_test_type_id, result, dictionary):
        self.id = id
        self.version = 0
        self.donor_id = dictionary['visit.donorId']
        self.visit_id = dictionary['visit.id']
        self.screening_test_type_id = screening_test_type_id
        self.result_value = result
        self.result_modifier = None
        self.result_actual = result
        self.result_assessment_ind = 'OK'
        self.result_ts = dictionary['visit.visitDate'] + '09.00.00.000000000 AM'
        self.created_in_tz = dictionary['visit.siteTimezone']
        self.actions_taken_flag = 0
        self.triggered_actions_type = 'NORMAL'
        self.baseline = 0
        self.escalated_visit = 0
        self.is_overridable = 0
        self.override_user_id = None
        self.schedule_reason = None

    @staticmethod
    def export_path():
        return '/visit/dnr$screening_tests/screening_tests.csv'

    @staticmethod
    def csv_header():
        return [
            '#dnr$screening_tests.id',
            '#dnr$screening_tests.version',
            '#dnr$screening_tests.donor_id',
            '#dnr$screening_tests.visit_id',
            '#dnr$screening_tests.scrntype_id',
            '#dnr$screening_tests.result_value',
            '#dnr$screening_tests.result_assess_ind',
            '#dnr$screening_tests.result_ts',
            '#dnr$screening_tests.created_in_tz',
            '#dnr$screening_tests.actions_taken_flag',
            '#dnr$screening_tests.triggered_actions_type',
            '#dnr$screening_tests.baseline',
            '#dnr$screening_tests.escalated_visit',
            '#dnr$screening_tests.override_userid',
            '#dnr$screening_tests.is_overridable',
            '#dnr$screening_tests.schedule_reason',
            '#dnr$screening_tests.result_modifier',
            '#dnr$screening_tests.result_actual'
        ]

    def csv_row(self):
        return {
            '#dnr$screening_tests.id':self.id,
            '#dnr$screening_tests.version':self.version,
            '#dnr$screening_tests.donor_id':self.donor_id,
            '#dnr$screening_tests.visit_id':self.visit_id,
            '#dnr$screening_tests.scrntype_id':self.screening_test_type_id,
            '#dnr$screening_tests.result_value':self.result_value,
            '#dnr$screening_tests.result_assess_ind':self.result_assessment_ind,
            '#dnr$screening_tests.result_ts':self.result_ts,
            '#dnr$screening_tests.created_in_tz':self.created_in_tz,
            '#dnr$screening_tests.actions_taken_flag':self.actions_taken_flag,
            '#dnr$screening_tests.triggered_actions_type':self.triggered_actions_type,
            '#dnr$screening_tests.baseline':self.baseline,
            '#dnr$screening_tests.escalated_visit':self.escalated_visit,
            '#dnr$screening_tests.override_userid':self.override_user_id,
            '#dnr$screening_tests.is_overridable':self.is_overridable,
            '#dnr$screening_tests.schedule_reason':self.schedule_reason,
            '#dnr$screening_tests.result_modifier':self.result_modifier,
            '#dnr$screening_tests.result_actual':self.result_actual
        }