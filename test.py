
from faker import Faker
import pandas as pd
import numpy as np
import random

fake = Faker("fr_FR")
df = pd.read_csv("CSV/adresse.csv")

sample_list = ["espece", "cheque", "CB"]
data = {}
for i in range(0, int(1000)):
        data[i]={}
        data[i]['nbr_de_places'] = random.randint(20, 100)
        data[i]['espace_enfant'] = random.randint(0, 1)
        data[i]['service_de_payement'] = np.random.choice(sample_list)
        data[i]['accessebilite_mobilite_reduite'] = random.randint(0, 1)
        data[i]['parking'] = random.randint(0, 1)
        data[i]['numero_tel_resto'] = fake.phone_number()
        data[i]['siret'] = random.randint(10000000000, 100000000000)
df1 = pd.DataFrame(data).T
df1['id_resto'] = df['id_resto']

df1.to_csv('CSV/Restaurant.csv', index=False)