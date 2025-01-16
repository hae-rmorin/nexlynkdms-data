from classes.Record import *

#InterviewResponse
class InterviewResponse(Record):
    def __init__(self, interview, question_id, dictionary):
        super().__init__(id)
        self.interview_id = interview.id
        self.question_id = question_id
        self.seq = None
        self.response_ts = None
        self.status_ind = None
        self.resource_status_ind = None
        self.completed_by = None
        self.completed_by_type = None
        self.comments = None

    @staticmethod
    def export_path():
        return '/interview/int$intv_responses/intv_responses.csv'

    @staticmethod
    def csv_header():
        return [
            '#int$intv_responses.id',
            '#int$intv_responses.version',
            '#int$intv_responses.intv_id',
            '#int$intv_responses.qst_id',
            '#int$intv_responses.seq',
            '#int$intv_responses.response_ts',
            '#int$intv_responses.status_ind',
            '#int$intv_responses.resource_status_ind',
            '#int$intv_responses.completed_by_id',
            '#int$intv_responses.completed_by_type',
            '#int$intv_responses.comments'
        ]

    def csv_row(self):
        return {
            '#int$intv_responses.id':self.id,
            '#int$intv_responses.version':self.version,
            '#int$intv_responses.intv_id':self.interview_id,
            '#int$intv_responses.qst_id':self.question_id,
            '#int$intv_responses.seq':self.seq,
            '#int$intv_responses.response_ts':self.response_ts,
            '#int$intv_responses.status_ind':self.status_ind,
            '#int$intv_responses.resource_status_ind':self.resource_status_ind,
            '#int$intv_responses.completed_by_id':self.completed_by_id,
            '#int$intv_responses.completed_by_type':self.completed_by_type,
            '#int$intv_responses.comments':self.comments
        }