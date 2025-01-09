#Screening Test

class ScreeningTest:
    def __init__(self, id, donor_id, visit_id, dictionary):
        self.id = id
        self.version = 0
        self.donor_id = donor_id
        self.visit_id = visit_id
        self.screening_test_type_id = None
        self.result_value = None
        self.result_modifier = None
        self.result_actual = None
        self.result_assessment_ind = None
        self.result_ts = None
        self.created_in_tz = None
        self.actions_taken_flag = None
        self.triggered_actions_type = None
        self.baseline = None
        self.escalated_visit = None
        self.is_overridable = None
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


#end of class definition

def build_screening_test(self, type_code, visit, properties):
    match type_code:
        case 'BP-SYS':
            self.screening_test_type_id = properties['screeningTests.bp-sys.screeningTestTypeId']
            self.result_value = properties['screeningTests.bp-sys.resultValue']
            self.result_modifier = properties['screeningTests.bp-sys.resultModifier']
            self.result_actual = properties['screeningTests.bp-sys.resultActual']
            self.result_assessment_ind = properties['screeningTests.bp-sys.resultAssessmentInd']
        case 'BP-DIA':
            self.screening_test_type_id = properties['screeningTests.bp-dia.screeningTestTypeId']
            self.result_value = properties['screeningTests.bp-dia.resultValue']
            self.result_modifier = properties['screeningTests.bp-dia.resultModifier']
            self.result_actual = properties['screeningTests.bp-dia.resultActual']
            self.result_assessment_ind = properties['screeningTests.bp-dia.resultAssessmentInd']
        case 'PUL':
            self.screening_test_type_id = properties['screeningTests.pulse.screeningTestTypeId']
            self.result_value = properties['screeningTests.pulse.resultValue']
            self.result_modifier = properties['screeningTests.pulse.resultModifier']
            self.result_actual = properties['screeningTests.pulse.resultActual']
            self.result_assessment_ind = properties['screeningTests.pulse.resultAssessmentInd']
        case 'TEMP':
            self.screening_test_type_id = properties['screeningTests.temp.screeningTestTypeId']
            self.result_value = properties['screeningTests.temp.resultValue']
            self.result_modifier = properties['screeningTests.temp.resultModifier']
            self.result_actual = properties['screeningTests.temp.resultActual']
            self.result_assessment_ind = properties['screeningTests.temp.resultAssessmentInd']
        case 'HCT':
            self.screening_test_type_id = properties['screeningTests.hct.screeningTestTypeId']
            self.result_value = properties['screeningTests.hct.resultValue']
            self.result_modifier = properties['screeningTests.hct.resultModifier']
            self.result_actual = properties['screeningTests.hct.resultActual']
            self.result_assessment_ind = properties['screeningTests.hct.resultAssessmentInd']
        case 'TP':
            self.screening_test_type_id = properties['screeningTests.tp.screeningTestTypeId']
            self.result_value = properties['screeningTests.tp.resultValue']
            self.result_modifier = properties['screeningTests.tp.resultModifier']
            self.result_actual = properties['screeningTests.tp.resultActual']
            self.result_assessment_ind = properties['screeningTests.tp.resultAssessmentInd']
        case 'HT':
            self.screening_test_type_id = properties['screeningTests.ht.screeningTestTypeId']
            self.result_value = properties['screeningTests.ht.resultValue']
            self.result_modifier = properties['screeningTests.ht.resultModifier']
            self.result_actual = properties['screeningTests.ht.resultActual']
            self.result_assessment_ind = properties['screeningTests.ht.resultAssessmentInd']
        case 'WT':
            self.screening_test_type_id = properties['screeningTests.wt.screeningTestTypeId']
            self.result_value = properties['screeningTests.wt.resultValue']
            self.result_modifier = properties['screeningTests.wt.resultModifier']
            self.result_actual = properties['screeningTests.wt.resultActual']
            self.result_assessment_ind = properties['screeningTests.wt.resultAssessmentInd']
        case 'ARM':
            self.screening_test_type_id = properties['screeningTests.arm.screeningTestTypeId']
            self.result_value = properties['screeningTests.arm.resultValue']
            self.result_modifier = properties['screeningTests.arm.resultModifier']
            self.result_actual = properties['screeningTests.arm.resultActual']
            self.result_assessment_ind = properties['screeningTests.arm.resultAssessmentInd']
    self.donor_id = visit.donor_id
    self.visit_id = visit.id
    self.baseline = properties['screeningTests.baseline']
    self.result_ts = properties['screeningTests.resultTs']
    self.created_in_tz = properties['screeningTests.createdInTz']
    self.escalated_visit = properties['screeningTests.escalatedVisit']
    self.is_overridable = properties['screeningTests.isOverridable']
    self.override_user_id = properties['screeningTests.overrideUserId']
    self.schedule_reason = properties['screeningTests.scheduleReason']
    self.actions_taken_flag = properties['screeningTests.actionsTakenFlag']
    self.triggered_actions_type = properties['screeningTests.triggeredActionsType']
    return self
#end of function definition
