
from faker import Faker
import pandas as pd
import numpy as np
import random
import datetime
from faker_food import FoodProvider
import uuid


fake = Faker("fr_FR")
fake.add_provider(FoodProvider)


# #     "Association",
# #     metadata,
# #     db.Column("id_association", db.Integer(), primary_key = True),
# #     db.Column("id_ingredient", db.Integer(), db.ForeignKey("Restaurant.id_resto")),
# #     db.Column("id_item", db.String(35), nullable=False),
 

data = {}
for i in range(0, int(100)):
        data[i]={}
        data[i]['id_association'] = uuid.uuid4()



df1 = pd.DataFrame(data).T

ingredient = pd.read_csv("CSV/ingredients.csv")
itms = pd.read_csv("CSV/items.csv")


df1['id_ingredient'] = ingredient['id_ingredient']
df1['id_item'] = itms['id_item']



# # df1.to_csv("CSV/ingredients.csv", index=False)



