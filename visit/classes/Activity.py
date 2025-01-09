from classes.Record import *

#Activity
#this class is 'abstract' and should not be instantiated explicitly, rather only it's subclasses
class Activity(Record):
    def __init__(self, id, dictionary):
        super().__init__(id)
        self.visit_id = dictionary['visit.id']
        self.donor_id = dictionary['visit.donorId']
        self.result_ts = dictionary['visit.visitDate'] + ' 09.00.00.000000000 AM'
        self.created_in_tz = dictionary['visit.siteTimezone']
        self.schedule_reason = None
        self.actions_taken_flag = 0
        self.is_legacy = 0
        self.escalated_visit = 0
        self.is_external = 0