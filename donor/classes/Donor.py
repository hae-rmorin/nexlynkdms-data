from classes.Record import *

#Donor
class Donor(Record):
    def __init__(self, id, donor_number_id, address_id, name_id, dictionary):
        super().__init__(id)
        self.photo_full_id = None
        self.photo_thumbnail_id = None
        self.address_id = address_id
        self.name_id = name_id
        self.donor_number_id = donor_number_id
        self.program_id = dictionary['donor.programCode']
        self.program_enrollment_date = None
        self.birth_date = dictionary['donor.birthDate']
        self.language_ind = dictionary['donor.languageInd']
        self.gender_ind = dictionary['donor.genderInd']
        self.race_ind = None
        self.region_code = None
        self.abo_ind = None
        self.rh_ind = None
        self.height = None
        self.legacy_ind = None
        self.legacy_details_id = None
        self.site_id = dictionary['siteId']
        self.applicant_ts = None
        self.serum_reset_ts = None
        self.collection_type_code = dictionary['donor.collectionTypeCode']
        self.flag_new_samples = 0
        self.can_be_referred = 1
        self.kiosk_usage_ind = 'SLFINTRV'
        self.arm_restriction_ind = None
        self.arm_preference_ind = None
        self.vein_grading_ind = None
        self.donor_engage_system_id = None
        self.is_double_blind_height = 0
        self.arrival_ts = None
        self.bio_consent = None
        self.anniversary_date = None

    @staticmethod
    def export_path():
        return '/donor/dnr$donors/donors.csv'

    @staticmethod
    def csv_header():
        return ['#dnr$donors.id',
                '#dnr$donors.version',
                '#dnr$donors.photo_full_id',
                '#dnr$donors.photo_thumbnail_id',
                '#dnr$donors.donraddr_id',
                '#dnr$donors.donrname_id',
                '#dnr$donors.donrnum_id',
                '#dnr$donors.program_code_id',
                '#dnr$donors.program_enroll_date',
                '#dnr$donors.birth_date',
                '#dnr$donors.lang_ind',
                '#dnr$donors.gender_ind',
                '#dnr$donors.race_ind',
                '#dnr$donors.region_code',
                '#dnr$donors.abo_ind',
                '#dnr$donors.rh_ind',
                '#dnr$donors.height',
                '#dnr$donors.legacy_ind',
                '#dnr$donors.legacy_details_id',
                '#dnr$donors.site_id',
                '#dnr$donors.applicant_ts',
                '#dnr$donors.serum_reset_ts',
                '#dnr$donors.collection_type_code',
                '#dnr$donors.flag_new_samples',
                '#dnr$donors.can_be_referred',
                '#dnr$donors.kiosk_usage_ind',
                '#dnr$donors.arm_restriction_ind',
                '#dnr$donors.arm_preference_ind',
                '#dnr$donors.vein_grading_ind',
                '#dnr$donors.dnr_engage_systm_id',
                '#dnr$donors.is_double_blind_height',
                '#dnr$donors.arrival_ts',
                '#dnr$donors.bio_consent',
                '#dnr$donors.anniversary_date'
            ]

    def csv_row(self):
        return {
                '#dnr$donors.id':self.id,
                '#dnr$donors.version':self.version,
                '#dnr$donors.photo_full_id':self.photo_full_id,
                '#dnr$donors.photo_thumbnail_id':self.photo_thumbnail_id,
                '#dnr$donors.donraddr_id':self.address_id,
                '#dnr$donors.donrname_id':self.name_id,
                '#dnr$donors.donrnum_id':self.donor_number_id,
                '#dnr$donors.program_code_id':self.program_id,
                '#dnr$donors.program_enroll_date':self.program_enrollment_date,
                '#dnr$donors.birth_date':self.birth_date,
                '#dnr$donors.lang_ind':self.language_ind,
                '#dnr$donors.gender_ind':self.gender_ind,
                '#dnr$donors.race_ind':self.race_ind,
                '#dnr$donors.region_code':self.region_code,
                '#dnr$donors.legacy_ind':self.legacy_ind,
                '#dnr$donors.legacy_details_id':self.legacy_details_id,
                '#dnr$donors.site_id':self.site_id,
                '#dnr$donors.applicant_ts':self.applicant_ts,
                '#dnr$donors.serum_reset_ts':self.serum_reset_ts,
                '#dnr$donors.collection_type_code':self.collection_type_code,
                '#dnr$donors.flag_new_samples':self.flag_new_samples,
                '#dnr$donors.can_be_referred':self.can_be_referred,
                '#dnr$donors.kiosk_usage_ind':self.kiosk_usage_ind,
                '#dnr$donors.arm_restriction_ind':self.arm_restriction_ind,
                '#dnr$donors.arm_preference_ind':self.arm_preference_ind,
                '#dnr$donors.vein_grading_ind':self.vein_grading_ind,
                '#dnr$donors.dnr_engage_systm_id':self.donor_engage_system_id,
                '#dnr$donors.is_double_blind_height':self.is_double_blind_height,
                '#dnr$donors.arrival_ts':self.arrival_ts,
                '#dnr$donors.bio_consent':self.bio_consent,
                '#dnr$donors.anniversary_date':self.anniversary_date
        }