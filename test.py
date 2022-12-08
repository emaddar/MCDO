
from faker import Faker
import pandas as pd
import numpy as np
import random
import datetime

fake = Faker("fr_FR")







# sample_list = ["directeur", "manager", "employee"]
data = {}
for i in range(0, int(1000)):
        data[i]={}
        data[i]['num_de_transaction'] = i
        data[i]['mois'] = random.randint(1, 12)
        data[i]['annee'] = random.randint(1990, 2022)
        data[i]['nbr_heures_de_tavail'] = random.randint(25, 35)
        data[i]['montant_historique'] = random.randint(900, 1600)
        data[i]['note_manager'] = random.randint(6, 10)

df1 = pd.DataFrame(data).T

df = pd.read_csv("CSV/personnels.csv")
df1["id_personnel"] = df['id_personnel']
# print(df1.head())
df1.to_csv("CSV/comptabilite.csv", index=False)