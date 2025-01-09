#Review
from visit.classes.Activity import Activity

class Review(Activity):
    def __init__(self, id, donor_id, visit_id, dictionary):
        super().__init__(id, donor_id, visit_id)
        self.review_type_id = dictionary['']
        self.ref_number = None
        self.custom_result_ind = None

    @staticmethod
    def export_path():
        return '/visit/dnr$reviews/reviews.csv'

    @staticmethod
    def csv_header():
        return [
            '#dnr$reviews.id',
            '#dnr$reviews.version',
            '#dnr$reviews.donor_id',
			'#dnr$reviews.visit_id',
            '#dnr$reviews.revtype_id',
            '#dnr$reviews.schedule_reason',
            '#dnr$reviews.result_value',
            '#dnr$reviews.result_assess_ind',
            '#dnr$reviews.result_ts',
            '#dnr$reviews.created_in_tz',
            '#dnr$reviews.is_legacy',
            '#dnr$reviews.ref_num',
            '#dnr$reviews.actions_taken_flag',
            '#dnr$reviews.escalated_visit',
            '#dnr$reviews.is_external',
            '#dnr$reviews.custom_result_ind'
        ]

    def csv_row(self):
        return {
            '#dnr$reviews.id':self.id,
            '#dnr$reviews.version':self.version,
            '#dnr$reviews.donor_id':self.donor_id,
            '#dnr$reviews.visit_id':self.visit_id,
            '#dnr$reviews.revtype_id':self.review_type_id,
            '#dnr$reviews.schedule_reason':self.schedule_reason,
            '#dnr$reviews.result_value':self.result_value,
            '#dnr$reviews.result_assess_ind':self.result_assessment_ind,
            '#dnr$reviews.result_ts':self.result_ts,
            '#dnr$reviews.created_in_tz':self.created_in_tz,
            '#dnr$reviews.is_legacy':self.is_legacy,
            '#dnr$reviews.ref_num':self.ref_number,
            '#dnr$reviews.actions_taken_flag':self.actions_taken_flag,
            '#dnr$reviews.escalated_visit':self.escalated_visit,
            '#dnr$reviews.is_external':self.is_external,
            '#dnr$reviews.custom_result_ind':self.custom_result_ind
        }