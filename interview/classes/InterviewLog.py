#InterviewLog
class InterviewLog:
    def __init__(self, interview):
        self.interview_id = interview.id
        self.action_ind = None
        self.log_text = None
        self.log_ts = None
        self.user_id = None

    @staticmethod
    def export_path():
        return 'interview/int$intv_log/intv_log.csv'

    @staticmethod
    def csv_header():
        return [
            '#int$intv_log.intv_id',
            '#int$intv_log.action_ind',
            '#int$intv_log.log_text',
            '#int$intv_log.log_ts',
            '#int$intv_log.user_id'
        ]

    def csv_row(self):
        return {
            '#int$intv_log.intv_id':self.interview_id,
            '#int$intv_log.action_ind':self.action_ind,
            '#int$intv_log.log_text':self.log_text,
            '#int$intv_log.log_ts':self.log_ts,
            '#int$intv_log.user_id':self.user_id
        }