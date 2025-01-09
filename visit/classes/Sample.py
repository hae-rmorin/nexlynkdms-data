#Sample
from visit.classes.Activity import Activity

class Sample(Activity):
    def __init__(self, id, donor_id, visit_id, sample_number, dictionary):
        super().__init__(id, donor_id, visit_id)
        self.sample_type_id = dictionary['']
        self.sample_number = sample_number

    @staticmethod
    def export_path():
        return '/visit/dnr$samples/samples.csv'

    @staticmethod
    def csv_header():
        return [
            '#dnr$samples.id',
            '#dnr$samples.version',
            '#dnr$samples.donor_id',
            '#dnr$samples.visit_id',
            '#dnr$samples.samptype_id',
            '#dnr$samples.sample_num',
            '#dnr$samples.schedule_reason',
            '#dnr$samples.result_ind',
            '#dnr$samples.result_assess_ind',
            '#dnr$samples.result_ts',
            '#dnr$samples.created_in_tz',
            '#dnr$samples.is_legacy',
            '#dnr$samples.actions_taken_flag',
            '#dnr$samples.escalated_visit',
            '#dnr$samples.is_external'
        ]

    def csv_row(self):
        return {
            '#dnr$samples.id':self.id,
            '#dnr$samples.version':self.version,
            '#dnr$samples.donor_id':self.donor_id,
            '#dnr$samples.visit_id':self.visit_id,
            '#dnr$samples.samptype_id':self.sample_type_id,
            '#dnr$samples.sample_num':self.sample_number,
            '#dnr$samples.schedule_reason':self.schedule_reason,
            '#dnr$samples.result_ind':self.result_value,
            '#dnr$samples.result_assess_ind':self.result_assessment_ind,
            '#dnr$samples.result_ts':self.result_ts,
            '#dnr$samples.created_in_tz':self.created_in_tz,
            '#dnr$samples.is_legacy':self.is_legacy,
            '#dnr$samples.actions_taken_flag':self.actions_taken_flag,
            '#dnr$samples.escalated_visit':self.escalated_visit,
            '#dnr$samples.is_external':self.is_external
        }