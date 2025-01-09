#Physical
from visit.classes.Activity import Activity

class Physical(Activity):
    def __init__(self, id, donor_id, visit_id, dictionary):
        super().__init__(id, donor_id, visit_id)
        self.physical_type_id = dictionary['']

    @staticmethod
    def export_path():
        return '/visit/dnr$physicals/physicals.csv'

    @staticmethod
    def csv_header():
        return [
            '#dnr$physicals.id',
            '#dnr$physicals.version',
            '#dnr$physicals.donor_id',
            '#dnr$physicals.visit_id',
            '#dnr$physicals.phystype_id',
            '#dnr$physicals.schedule_reason',
            '#dnr$physicals.result_value',
            '#dnr$physicals.result_assess_ind',
            '#dnr$physicals.result_ts',
            '#dnr$physicals.created_in_tz',
            '#dnr$physicals.is_legacy',
            '#dnr$physicals.actions_taken_flag',
            '#dnr$physicals.escalated_visit',
            '#dnr$physicals.is_external'
        ]

    def csv_row(self):
        return {
            '#dnr$physicals.id':self.id,
            '#dnr$physicals.version':self.version,
            '#dnr$physicals.donor_id':self.donor_id,
            '#dnr$physicals.visit_id':self.visit_id,
            '#dnr$physicals.phystype_id':self.physical_type_id,
            '#dnr$physicals.schedule_reason':self.schedule_reason,
            '#dnr$physicals.result_value':self.result_value,
            '#dnr$physicals.result_assess_ind':self.result_assessment_ind,
            '#dnr$physicals.result_ts':self.result_ts,
            '#dnr$physicals.created_in_tz':self.created_in_tz,
            '#dnr$physicals.is_legacy':self.is_legacy,
            '#dnr$physicals.actions_taken_flag':self.actions_taken_flag,
            '#dnr$physicals.escalated_visit':self.escalated_visit,
            '#dnr$physicals.is_external':self.is_external
        }