import random
from string import digits
from util.string_util import generate_random_string

# this function returns a random entry from the list of genders
def random_gender():
    choices = ['F', 'M']
    return random.choice(choices)
# end of random_gender

# this function returns a random entry from the list of ethnicities
def random_ethnicity():
    choices = ['AM', 'ASIAN', 'CASIAN', 'NATIVE']
    return random.choice(choices)
# end of random_ethnicity

# this function returns a random ssn identification in the format 'XXX-XX-XXXX'
def random_ssn():
    return generate_random_string(digits, 3) + '-' + generate_random_string(digits, 2) + '-' + generate_random_string(
        digits, 4)
# end of random_ssn

# this function returns a random string of alphanumerics of length determined by the argument 'length'
def random_identification(length):
    return ''.join(random.choice('0123456789ABCDEF') for i in range(length))
# end of random_identification


# this function returns