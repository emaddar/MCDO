
from faker import Faker
import pandas as pd
import numpy as np
import random
import datetime
from faker_food import FoodProvider


fake = Faker("fr_FR")
fake.add_provider(FoodProvider)


#     "Carte",
#     metadata,
#     db.Column("pays_resto", db.Integer(), primary_key = True),
#     db.Column("id_items", db.Integer(), db.ForeignKey("Restaurant.id_resto")),
#     db.Column("id_menu", db.String(35), nullable=False),



df1 = pd.DataFrame()
resto = pd.read_csv("CSV/adresse.csv")
menu = pd.read_csv("CSV/menu.csv")
itms = pd.read_csv("CSV/items.csv")

df1['pays_resto'] = resto['pays_resto']
df1['id_item'] = itms['id_item']
df1['id_menu'] = menu['id_menu']
print(df1.head())
# df1.to_csv("CSV/carte.csv", index=False)