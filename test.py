
from faker import Faker
import pandas as pd
import numpy as np
import random
import datetime
from faker_food import FoodProvider
import uuid


fake = Faker("fr_FR")
fake.add_provider(FoodProvider)

#     "Facture_association",
#     metadata,

#     db.Column("id_association", db.Integer(), primary_key = True),
#     db.Column("id_ingredient", db.Integer(), db.ForeignKey("Ingredients.id_ingredient")),
#     db.Column("id_item", db.String(35), db.ForeignKey("Items.id_item")),
 

sample_list = ["CB", "espece", "cheque"]

data = {}
for i in range(0, int(1000)):
        data[i]={}
        data[i]['id_association'] =  uuid.uuid4()
        data[i]['date'] =fake.date_between(start_date="-70y",end_date="-0y")
        data[i]['heure'] = f"{random.randint(9,11)}:{random.randint(0,59)}:{random.randint(0,59)}"
        data[i]['payement_type'] = np.random.choice(sample_list)
        data[i]['borne'] =random.randint(0,1)
        data[i]['prix_total'] =  random.randint(5, 200)


df1 = pd.DataFrame(data).T
perso = pd.read_csv("CSV/personnels.csv")
menu = pd.read_csv("CSV/menu.csv")
resto = pd.read_csv("CSV/Restaurant.csv")


# resto = pd.read_csv("CSV/Restaurant.csv")
# ing = pd.read_csv("CSV/ingredients.csv")
itms = pd.read_csv("CSV/items.csv")


df1['id_personnel'] = perso['id_personnel']
df1['nom_item'] = itms['nom_item']
df1['prix_vente_item'] = itms['prix_vente_item']
df1['prix_vente_menu'] = menu['prix_vente_menu']
df1['id_resto'] = resto['id_resto']



# df1.to_csv("CSV/facture.csv", index=False)
print(df1.columns)


