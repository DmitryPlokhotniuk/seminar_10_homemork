import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()


names = data['whoAmI'].unique()
new_data = pd.DataFrame()
for value in names:
    new_data[value] = (data['whoAmI'] == value).astype(int)
print(new_data)
