from classes.Record import *

#Name
class Name(Record):
    def __init__(self, id, donor_id, dictionary):
        super().__init__(id)
        self.donor_id = donor_id
        self.name_first = dictionary['name.first']
        self.name_last = dictionary['name.last']
        self.name_middle = dictionary['name.middle']
        self.name_suffix = dictionary['name.suffix']
        self.recorded_ts = None
        self.dbl_meta_name_first_primary = None
        self.dbl_meta_name_last_primary = None
        self.dbl_meta_name_middle_primary = None
        self.dbl_meta_name_first_secondary = None
        self.dbl_meta_name_last_secondary = None
        self.dbl_meta_name_middle_secondary = None
        self.modified_by = None

    @staticmethod
    def export_path():
        return '/donor/dnr$names/names.csv'

    @staticmethod
    def csv_header():
        return [
            '#dnr$names.id',
            '#dnr$names.version',
            '#dnr$names.donor_id',
            '#dnr$names.name_first',
            '$dnr$names.name_middle',
            '#dnr$names.name_last',
            '$dnr$names.name_suffix',
            '#dnr$names.recorded_ts',
            '#dnr$names.dbl_meta_name_first_primary',
            '#dnr$names.dbl_meta_name_first_secondary',
            '#dnr$names.db1_meta_name_middle_primary',
            '#dnr$names.db1_meta_name_middle_secondary',
            '#dnr$names.db1_meta_name_last_primary',
            '#dnr$names.db1_meta_name_last_secondary',
            '#dnr$names.modified_by'
        ]

    def csv_row(self):
        return {
            '#dnr$names.id':self.id,
            '#dnr$names.version':self.version,
            '#dnr$names.donor_id':self.donor_id,
            '#dnr$names.name_first':self.name_first,
            '$dnr$names.name_middle':self.name_middle,
            '#dnr$names.name_last':self.name_last,
            '$dnr$names.name_suffix':self.name_suffix,
            '#dnr$names.recorded_ts':self.recorded_ts,
            '#dnr$names.dbl_meta_name_first_primary':self.dbl_meta_name_first_primary,
            '#dnr$names.dbl_meta_name_first_secondary':self.dbl_meta_name_first_secondary,
            '#dnr$names.db1_meta_name_middle_primary':self.dbl_meta_name_middle_primary,
            '#dnr$names.db1_meta_name_middle_secondary':self.dbl_meta_name_middle_secondary,
            '#dnr$names.db1_meta_name_last_primary':self.dbl_meta_name_last_primary,
            '#dnr$names.db1_meta_name_last_secondary':self.dbl_meta_name_last_secondary,
            '#dnr$names.modified_by':self.modified_by
        }