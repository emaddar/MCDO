
from faker import Faker
import pandas as pd
import numpy as np
import random
import datetime
from faker_food import FoodProvider


fake = Faker("fr_FR")
fake.add_provider(FoodProvider)






sample_list = ["p", "m","l"]
dessert = ["Hot Fudge Sundae", "Baked Apple Pie", "Hot Caramel Sundae", "M&M McFlurry", "Strawberry Shake"]
data = {}
for i in range(0, int(1000)):
        data[i]={}
        data[i]['id_item'] = i
        data[i]['nom_item'] = fake.dish()
        data[i]['boisson_taille'] = np.random.choice(sample_list)
        data[i]['prix_vente_menu'] =  random.randint(2, 12)


df1 = pd.DataFrame(data).T

# print(df1.head())
df1.to_csv("CSV/items.csv", index=False)