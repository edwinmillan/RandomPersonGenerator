#!/usr/bin/env python3
import random_person
import csv


def generate_random_person_data():
    first_name = random_person.generate_first_name()
    middle_initial = random_person.generate_middle_initial()
    last_name = random_person.generate_last_name()
    full_name = '{} {} {}'.format(first_name, middle_initial, last_name)
    ssn = random_person.generate_ssn(full_name)
    dob = random_person.generate_date_of_birth()
    address = random_person.generate_address()
    dept_num = random_person.generate_dept_num()
    # Aggregate all the data into a dictionary.
    random_person_data = {
        'SSN': ssn,
        'DOB': dob,
        'Fname': first_name,
        'Minit': middle_initial,
        'Lname': last_name,
        'Address': address,
        'deptNum': dept_num
    }
    yield random_person_data


def main():
    amount_of_people = 2000
    data_filepath = 'output.csv'
    with open(data_filepath, 'w', newline='') as data_file:
        fieldnames = ['SSN', 'DOB', 'Fname', 'Minit', 'Lname', 'Address', 'deptNum']
        csv_writer = csv.DictWriter(data_file, fieldnames=fieldnames)
        csv_writer.writeheader()

        print('-'*100)  # Salt! (Flavor)
        for iteration in range(1, amount_of_people + 1):
            random_person_data = next(generate_random_person_data())
            print(iteration, random_person_data)
            csv_writer.writerow(random_person_data)
            print('-' * 100)  # And Pepper! (Flavor)


if __name__ == '__main__':
    main()
