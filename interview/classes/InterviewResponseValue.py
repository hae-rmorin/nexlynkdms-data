#InterviewResponseValue
class InterviewResponseValue:
    def __init__(self, interview_response):
        self.interview_response_id = interview_response.id
        self.question_option_id = None

    @staticmethod
    def export_path():
        return '/interview/int$intv_responses/intv_response_values.csv'

    @staticmethod
    def csv_header():
        return [
            '#int$intv_response_values.intvresp_id',
            '#int$intv_response_values.qstopt_id'
        ]

    def csv_row(self):
        return {
            '#int$intv_response_values.intvresp_id':self.interview_response_id,
            '#int$intv_response_values.qstopt_id':self.question_option_id
        }