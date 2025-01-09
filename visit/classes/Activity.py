from classes.Record.import *

#Activity
#this class is 'abstract' and should not be instantiated explicitly, rather only it's subclasses
class Activity(Record):
    def __init__(self, id, donor_id, visit_id):
        super().__init__(id)
        self.visit_id = visit_id
        self.donor_id = donor_id
        self.result_value = None
        self.result_assessment_ind = None
        self.result_ts = None
        self.created_in_tz = None
        self.schedule_reason = None
        self.actions_taken_flag = 0
        self.is_legacy = 0
        self.escalated_visit = 0
        self.is_external = 0
#end of class definition