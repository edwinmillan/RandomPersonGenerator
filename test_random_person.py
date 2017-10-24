import pytest
import random_person
import re


def clean_names(names):
    return [name.strip() for name in names]


@pytest.fixture()
def first_names():
    names = open('first_names.txt').readlines()
    return clean_names(names)


@pytest.fixture()
def last_names():
    names = open('last_names.txt').readlines()
    return clean_names(names)


def test_first_name_generator(first_names):
    name = random_person.generate_first_name()
    assert type(name) == str
    assert name in first_names


def test_middle_initial_generator():
    initial = random_person.generate_middle_initial()
    assert len(initial) == 2
    assert re.search('[A-Z]\.', initial)


def test_last_name_generator(last_names):
    name = random_person.generate_last_name()
    assert type(name) == str
    assert name in last_names


@pytest.mark.parametrize('middle_initial', [None, 'A.'])
def test_full_name_generator(middle_initial):
    name = random_person.generate_full_name(middle_initial=middle_initial)
    splitname = name.split(' ')
    assert type(name) == str
    if middle_initial:
        assert len(splitname) == 3
    else:
        assert len(splitname) == 2


def test_ssn_generator():
    name = 'John Doe'
    ssn = random_person.generate_ssn(name)
    assert type(ssn) == int
    assert ssn > 99999999
    assert ssn < 1000000000


def test_dob_generator():
    dob = random_person.generate_dob()
    month, day, year = dob.split('/')
    assert type(dob) == str
    assert int(month) in range(1, 12)
    assert int(day) in range(1, 29)
    assert int(year) in range(1900, 2017)


def test_address_generator():
    street_nums = range(1, 999)
    fruits = ['Apple', 'Banana', 'Orange', 'Grape', 'Mango']
    street_types = ['Lane', 'Street', 'Road']
    address = random_person.generate_address()
    num, fruit, street_type = address.split(' ')
    assert int(num) in street_nums
    assert fruit in fruits
    assert street_type in street_types
    assert type(address) == str


def test_department_number_generator():
    dept_num = random_person.generate_dept_num()
    assert type(dept_num) == int
    assert dept_num in range(1, 100000)
