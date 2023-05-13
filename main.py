from faker import Faker
fake = Faker(['en_IN'])

for _ in range(5):
    print("Phone Number", fake.phone_number())
    print("Country Code", fake.country_calling_code())
    print("MSISDN", fake.msisdn())
    print("")