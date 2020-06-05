from database import base
from faker import Faker

from models.pothole import Pothole

# Run
def run():
    print('Refreshing...')

    # Clear
    base.delete_tables()
    base.create_tables()

    # Define
    fake = Faker('es_ES')

    # Generate
    n = fake.pyint(min_value = 10, max_value = 30)

    print(f'Generating {n}... ')

    for i in range(n):
        # Seed
        Pothole.seed(fake)

    print('Seed tables [OK]')
