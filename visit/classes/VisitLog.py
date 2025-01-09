#VisitLog
class VisitLog:
    def __init__(self):
        self.visit_id = None
        self.log_text = None
        self.log_ts = None
        self.logged_by_user_id = None

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