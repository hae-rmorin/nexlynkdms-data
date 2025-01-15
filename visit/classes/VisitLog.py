#VisitLog
class VisitLog:
    def __init__(self, dictionary):
        self.visit_id = dictionary['visit.id']
        self.log_text = '\'Visit Closed\''
        self.log_ts = dictionary['visit.visitDate'] + ' 11.00.00.000000000 AM'
        self.logged_by_user_id = 'ADMIN'

    @staticmethod
    def export_path():
        return '/visit/dnr$visit_log/visit_log.csv'

    @staticmethod
    def csv_header():
        return [
            '#dnr$visit_log.visit_id',
            '#dnr$visit_log.log_text',
            '#dnr$visit_log.log_ts',
			'#dnr$visit_log.logged_by_userid'
        ]

    def csv_row(self):
        return {
            '#dnr$visit_log.visit_id':self.visit_id,
            '#dnr$visit_log.log_text':self.log_text,
            '#dnr$visit_log.log_ts':self.log_ts,
            '#dnr$visit_log.logged_by_userid':self.logged_by_user_id
        }