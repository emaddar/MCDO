from faker import Faker
import pandas as pd
import numpy as np
import random
import datetime
from faker_food import FoodProvider
import uuid


fake = Faker("fr_FR")
fake.add_provider(FoodProvider)


# facture_association_table = db.Table(
#     "Facture_association",
#     metadata,

#     db.Column("id_association", db.String(50), primary_key = True),
#     db.Column("id_facture", db.Integer(), db.ForeignKey("Facture.id_facture")),
#     db.Column("id_item", db.String(35), db.ForeignKey("Items.id_item")),
#     db.Column("id_menu", db.String(35), db.ForeignKey("Menu.id_menu")),
 
# )


data = {}
for i in range(0, int(1000)):
        data[i]={}
        data[i]['id_association_1'] =  uuid.uuid4()

df1 = pd.DataFrame(data).T
menu=pd.read_csv("CSV/menu.csv")
fact = pd.read_csv("CSV/facture.csv")



# resto = pd.read_csv("CSV/Restaurant.csv")
# ing = pd.read_csv("CSV/ingredients.csv")


df1['id_menu'] = menu['id_menu']
df1['id_facture'] = fact['id_facture']



df1.to_csv("CSV/facture_association_1.csv", index=False)