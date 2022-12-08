
from faker import Faker
import pandas as pd
import numpy as np
import random
import datetime
from faker_food import FoodProvider


fake = Faker("fr_FR")
fake.add_provider(FoodProvider)



sample_list = ["Coca", "Fanta", "Sprit", "Oasis"]
dessert = ["Hot Fudge Sundae", "Baked Apple Pie", "Hot Caramel Sundae", "M&M McFlurry", "Strawberry Shake"]
data = {}
for i in range(0, int(100)):
        data[i]={}
        data[i]['id_menu'] = i
        data[i]['plat'] = fake.dish()
        data[i]['boisson'] = np.random.choice(sample_list)
        data[i]['dessert'] = np.random.choice(dessert)
        data[i]['prix_vente_menu'] = random.randint(7, 14)


df1 = pd.DataFrame(data).T

print(df1.head())
df1.to_csv("CSV/menu.csv", index=False)