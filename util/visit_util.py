import random

def visit_number(donor_number, previous_visit_number):
    if previous_visit_number is None:
        return 'V' + donor_number + '-1'
    else:
        return previous_visit_number[:-1] + str(int(previous_visit_number[-1]) + 1)

#returns the random height in inches
def random_height():
    min = 60
    max = 78
    return random.randint(min, max)

#returns the random weight in pounds
def random_weight():
    min = 110
    max = 200
    return random.randint(min, max)

def random_bp_sys():
    min = 90
    max = 180
    return random.randint(min, max)

def random_bp_dia():
    min = 50
    max = 100
    return random.randint(min, max)

def random_pulse():
    min = 50
    max = 100
    return random.randint(min, max)

def random_hct():
    min = 39
    max = 54
    return random.randint(min, max)

def random_tp():
    min = 60
    max = 90
    return random.randrange(min, max) / 10

def random_temp():
    min = 950
    max = 995
    return random.randrange(min, max) / 10

def activity_result(activity):
    if isinstance(activity, Consent):
        return 'ACCEPTED'
    else:
        return 'PASS'