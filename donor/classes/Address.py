from classes.Record import *

#Address
class Address(Record):
    def __init__(self, id, donor_id, dictionary):
        super().__init__(id)
        self.donor_id = donor_id
        self.addr1 = dictionary['address.addr1']
        self.addr2 = dictionary['address.addr2']
        self.city = dictionary['address.city']
        self.province = dictionary['address.state']
        self.country = dictionary['address.country']
        self.postal_code = dictionary['address.zip']
        self.recorded_ts = None
        self.latitude = None
        self.longitude = None
        self.suitability_type_ind = None
        self.modified_by = None
        self.postal_code_lower = None
        self.city_lower = None
        self.province_lower = None
        self.country_lower = None
        self.addr1_lower = None
        self.addr2_lower = None
        self.suit_determined_by = None
        self.suit_determined_ts = None
        self.match_overridden_by = None

    @staticmethod
    def export_path():
        return '/donor/dnr$addresses/addresses.csv'

    @staticmethod
    def csv_header():
        return [
            '#dnr$addresses.id',
            '#dnr$addresses.version',
            '#dnr$addresses.donor_id',
            '#dnr$addresses.addr1',
            '#dnr$addresses.addr2',
            '#dnr$addresses.city',
            '#dnr$addresses.province',
            '#dnr$addresses.country',
            '#dnr$addresses.postal_code',
            '#dnr$addresses.recorded_ts',
            '#dnr$addresses.latitude',
            '#dnr$addresses.longitude',
            '#dnr$addresses.suitability_type_ind',
            '#dnr$addresses.modified_by',
            '#dnr$addresses.postal_code_lower',
            '#dnr$addresses.city_lower',
            '#dnr$addresses.country_lower',
            '#dnr$addresses.province_lower',
            '#dnr$addresses.addr1_lower',
            '#dnr$addresses.addr2_lower',
            '#dnr$addresses.suit_determined_by',
            '#dnr$addresses.suit_determined_ts',
            '#dnr$addresses.match_overridden_by'
        ]

    def csv_row(self):
        return {
            '#dnr$addresses.id':self.id,
            '#dnr$addresses.version':self.version,
            '#dnr$addresses.donor_id':self.donor_id,
            '#dnr$addresses.addr1':self.addr1,
            '#dnr$addresses.addr2':self.addr2,
            '#dnr$addresses.city':self.city,
            '#dnr$addresses.province':self.province,
            '#dnr$addresses.country':self.country,
            '#dnr$addresses.postal_code':self.postal_code,
            '#dnr$addresses.recorded_ts':self.recorded_ts,
            '#dnr$addresses.latitude':self.latitude,
            '#dnr$addresses.longitude':self.longitude,
            '#dnr$addresses.suitability_type_ind':self.suitability_type_ind,
            '#dnr$addresses.modified_by':self.modified_by,
            '#dnr$addresses.postal_code_lower':self.postal_code_lower,
            '#dnr$addresses.city_lower':self.city_lower,
            '#dnr$addresses.country_lower':self.country_lower,
            '#dnr$addresses.province_lower':self.province_lower,
            '#dnr$addresses.addr1_lower':self.addr1_lower,
            '#dnr$addresses.addr2_lower':self.addr2_lower,
            '#dnr$addresses.suit_determined_by':self.suit_determined_by,
            '#dnr$addresses.suit_determined_ts':self.suit_determined_ts,
            '#dnr$addresses.match_overridden_by':self.match_overridden_by
        }