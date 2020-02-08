import csv
import sys
from typing import TextIO,Dict, Any, Union

bank_data_file: TextIO
with open('data/bank-data.csv') as bank_data_file:
    bank_data = list(csv.DictReader(bank_data_file))

# find the etrema for customers age
customer_ages = list(bank_datae['age'] for bank_datae in bank_data)
age_extrema = {'min': min(customer_ages), 'max': max(customer_ages)}
print(age_extrema)

# store unique professions
unique_professions = set(bank_datae['job'].lower() for bank_datae in bank_data)
print(unique_professions)

# is client has a eligible profession?
while True:
    user_input = input("Enter profession: ")
    if user_input == "END": break
    is_profession_found = user_input.lower() in unique_professions
    print("eligible" if is_profession_found else "non eligible")