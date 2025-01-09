from classes.Record import *

#Visit
class Visit(Record):
    def __init__(self, id, donor_id, dictionary):
        super().__init__(id)
        self.donor_id = donor_id
        self.visit_number = None
        self.site_id = dictionary['siteId']
        self.program_id = None
        self.visit_type_id = None
        self.collection_type_code = None
        self.status_ind = None
        self.checkin_ts = None
        self.checkout_ts = None
        self.fingerstick_ts = None
        self.screening_form_id = None
        self.donor_suitability_ruleset_id = None
        self.collection_number = None
        self.language_ind = None
        self.is_donation_completed = None
        self.ppta_report_class_ind = None
        self.visit_date = None
        self.donor_suitability_result_ind = None
        self.donor_suitability_comment = None
        self.is_ppta_reportable = None
        self.is_ppta_tested = None
        self.is_ppta_reactive = None
        self.is_cancel_required = None
        self.reason_to_cancel = None
        self.is_vip_visit = None
        self.is_escalated = None
        self.ema_report_class_ind = None
        self.escalation_reason = None
        self.is_visit_cancelled = None
        self.bio_consent = None

    @staticmethod
    def export_path():
        return '/visit/dnr$visits/visits.csv'

    @staticmethod
    def csv_header():
        return  [
            '#dnr$visits.id',
            '#dnr$visits.version',
            '#dnr$visits.donor_id',
			'#dnr$visits.site_id',
            '#dnr$visits.visit_number',
            '#dnr$visits.program_id',
            '#dnr$visits.vsttype_id',
            '#dnr$visits.colltype_code',
            '#dnr$visits.status_ind',
            '#dnr$visits.checkin_ts',
            '#dnr$visits.checkout_ts',
            '#dnr$visits.fingerstick_ts',
            '#dnr$visits.scrnform_id',
            '#dnr$visits.dnrsuit_id',
            '#dnr$visits.coll_number',
            '#dnr$visits.lang_ind',
            '#dnr$visits.is_donation_completed',
            '#dnr$visits.ppta_report_class_ind',
            '#dnr$visits.visit_date',
            '#dnr$visits.dnrsuit_result_ind',
            '#dnr$visits.dnrsuit_comment',
            '#dnr$visits.is_ppta_reportable',
            '#dnr$visits.is_ppta_tested',
            '#dnr$visits.is_ppta_reactive',
            '#dnr$visits.is_cancel_required',
            '#dnr$visits.reason_to_cancel',
            '#dnr$visits.is_vip_visit',
            '#dnr$visits.is_escalated',
            '#dnr$visits.ema_report_class_ind',
            '#dnr$visits.escalation_reason',
            '#dnr$visits.is_visit_cancelled',
            '#dnr$visits.bio_consent'
        ]

    def csv_row(self):
        return {
            '#dnr$visits.id':self.id,
            '#dnr$visits.version':self.version,
            '#dnr$visits.donor_id':self.donor_id,
            '#dnr$visits.site_id':self.site_id,
            '#dnr$visits.visit_number':self.visit_number,
            '#dnr$visits.program_id':self.program_id,
            '#dnr$visits.vsttype_id':self.visit_type_id,
            '#dnr$visits.colltype_code':self.collection_type_code,
            '#dnr$visits.status_ind':self.status_ind,
            '#dnr$visits.checkin_ts':self.checkin_ts,
            '#dnr$visits.checkout_ts':self.checkout_ts,
            '#dnr$visits.fingerstick_ts':self.fingerstick_ts,
            '#dnr$visits.scrnform_id':self.screening_form_id,
            '#dnr$visits.dnrsuit_id':self.donor_suitability_ruleset_id,
            '#dnr$visits.coll_number':self.collection_number,
            '#dnr$visits.lang_ind':self.language_ind,
            '#dnr$visits.is_donation_completed':self.is_donation_completed,
            '#dnr$visits.ppta_report_class_ind':self.ppta_report_class_ind,
            '#dnr$visits.visit_date':self.visit_date,
            '#dnr$visits.dnrsuit_result_ind':self.donor_suitability_result_ind,
            '#dnr$visits.dnrsuit_comment':self.donor_suitability_comment,
            '#dnr$visits.is_ppta_reportable':self.is_ppta_reportable,
            '#dnr$visits.is_ppta_tested':self.is_ppta_tested,
            '#dnr$visits.is_ppta_reactive':self.is_ppta_reactive,
            '#dnr$visits.is_cancel_required':self.is_cancel_required,
            '#dnr$visits.reason_to_cancel':self.reason_to_cancel,
            '#dnr$visits.is_vip_visit':self.is_vip_visit,
            '#dnr$visits.is_escalated':self.is_escalated,
            '#dnr$visits.ema_report_class_ind':self.ema_report_class_ind,
            '#dnr$visits.escalation_reason':self.escalation_reason,
            '#dnr$visits.is_visit_cancelled':self.is_visit_cancelled,
            '#dnr$visits.bio_consent':self.bio_consent
        }