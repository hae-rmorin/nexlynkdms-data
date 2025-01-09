import random
from datetime import datetime, timedelta


# this function takes a pair of python dates ie: datetime(year,month,date)
# corresponding to the start date and end date of a range.
# the function will return a random date (string) in the format (date, month, year) ex: (01-Jan-1970)
def random_date_in_range(start_date, end_date):
    date_range = end_date - start_date
    random_days = random.randint(0, date_range.days)
    random_date = start_date + timedelta(days=random_days)
    return random_date.strftime('%d-%b-%y')
# end of random_date_in_range


def expiry_date_in_future(days):
    return (datetime.now() + timedelta(days=days)).strftime('%d-%b-%y')
#end of expiry_date_in_future