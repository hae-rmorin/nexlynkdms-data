#
class DataObject:
    def __init__(self):
        self.site_id = None

        self.new_donor = True

        #used in new_donor
        self.donor_id = None
        self.donor_birth_date = None
        self.donor_gender_ind = None
        self.donor_land_ind = None
        self.donor_program_code_id = None
        self.donor_collection_type_code = None
        self.donor_number = None
        self.donor_first_name = None
        self.donor_last_name = None

        # used in new_visit
        self.visit_id = None
        self.visit_number = None

        #used in new_interviews
        self.consent = None
        self.questionnaire = None
        self.physical = None


        # used in new_collection
        self.collection_number = None
        self.collection_id = None
