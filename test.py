
from faker import Faker
import pandas as pd
import numpy as np
import random
import datetime

fake = Faker("fr_FR")
# df = pd.read_csv("CSV/adresse.csv")

# sample_list = ["espece", "cheque", "CB"]
# data = {}
# for i in range(0, int(1000)):
#         data[i]={}
#         data[i]['nbr_de_places'] = random.randint(20, 100)
#         data[i]['espace_enfant'] = random.randint(0, 1)
#         data[i]['service_de_payement'] = np.random.choice(sample_list)
#         data[i]['accessebilite_mobilite_reduite'] = random.randint(0, 1)
#         data[i]['parking'] = random.randint(0, 1)
#         data[i]['numero_tel_resto'] = fake.phone_number()
#         data[i]['siret'] = random.randint(10000000000, 100000000000)
# df1 = pd.DataFrame(data).T
# df1['id_resto'] = df['id_resto']

# df1.to_csv('CSV/Restaurant.csv', index=False)


# df = pd.read_csv("CSV/personnels.csv")

sample_list = ["directeur", "manager", "employee"]
data = {}
for i in range(0, int(1000)):
        data[i]={}
        data[i]['id_personnel'] = i
        data[i]['nom'] = fake.last_name()
        data[i]['prenom'] = fake.last_name()
        data[i]['date_de_naissance'] = fake.date_between(start_date="-70y",end_date="-18y")
        data[i]['num_telephone_perso'] = fake.phone_number()
        data[i]['email'] = f"{data[i]['prenom']}.{data[i]['nom']}@{fake.domain_name()}"
        data[i]['rib'] = fake.iban()
        data[i]['adresse_perso'] = fake.address().replace('\n', ', ')
        data[i]['ville_perso'] = data[i]['adresse_perso'].split(" ")[-1]
        data[i]['code_postale_perso'] = data[i]['adresse_perso'].split(" ")[-2]
        data[i]['date_entree'] = fake.date_between(start_date="-30y",end_date="-2y")
        data[i]['status_employee'] =  np.random.choice(sample_list, p=[0.1, 0.4, 0.5])
        data[i]['en_formation'] = random.randint(0, 1)
        data[i]['nbr_de_changement_poste'] = random.randint(0, 5)
        data[i]['nbr_de_changement_resto'] = random.randint(0, 3)

df1 = pd.DataFrame(data).T

df = pd.read_csv("CSV/Restaurant.csv")
df1["id_resto"] = df['id_resto']
df1.to_csv("CSV/personnels.csv", index=False)