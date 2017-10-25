import random
import uuid


def generate_first_name():
    first_names = open('first_names.txt').readlines()
    first_name = random.choice(first_names).strip()
    return first_name


def generate_middle_initial():
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return '{}.'.format(random.choice(alphabet))


def generate_last_name():
    last_names = open('last_names.txt').readlines()
    last_name = random.choice(last_names).strip()
    return last_name


def generate_full_name(middle_initial=None):
    first_name = generate_first_name()
    last_name = generate_last_name()
    if middle_initial:
        return '{} {} {}'.format(first_name, middle_initial, last_name)
    else:
        return '{} {}'.format(first_name, last_name)


def generate_ssn(name, length=9):
    raw_id = uuid.uuid5(uuid.NAMESPACE_X500, name)
    int_id = raw_id.int
    sliced_id = str(int_id)[:length]
    ssn = int(sliced_id)
    return ssn


def generate_dept_num():
    return random.choice(range(1, 100000))


def generate_date_of_birth():
    month = random.choice(range(1, 12))
    day = random.choice(range(1, 29))  # Not going to implement any true date logic
    year = random.choice(range(1900, 2017))
    return '{}/{}/{}'.format(month, day, year)


def generate_address():
    street_num = str(random.choice(range(1, 999)))
    fruit = random.choice(['Apple', 'Banana', 'Orange', 'Grape', 'Mango'])
    street_type = random.choice(['Lane', 'Street', 'Road'])
    return '{} {} {}'.format(street_num, fruit, street_type)
