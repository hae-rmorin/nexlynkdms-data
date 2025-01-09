from classes.Record import *

#DonorNumber
class DonorNumber(Record):
    def __init__(self, id, donor_id, dictionary):
        super().__init__(id)
        self.donor_id = donor_id
        self.donor_number = str(dictionary['donor.donorNumber'].lstrip('0')).zfill(8)

    @staticmethod
    def export_path():
        return '/donor/dnr$donor_numbers/donor_numbers.csv'

    @staticmethod
    def csv_header():
        return [
            '#dnr$donor_numbers.id',
            '#dnr$donor_numbers.version',
            '#dnr$donor_numbers.donor_id',
            '#dnr$donor_numbers.donor_number'
        ]

    def csv_row(self):
        return {
            '#dnr$donor_numbers.id':self.id,
            '#dnr$donor_numbers.version':self.version,
            '#dnr$donor_numbers.donor_id':self.donor_id,
            '#dnr$donor_numbers.donor_number':self.donor_number
        }