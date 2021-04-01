import numpy as np
import pandas as pd
from apyori import apriori

data = pd.read_csv("apriori.csv")

nOfRow = data.shape[0]

# from panda DataFrame convert to a list
records = []
for i in range(data.shape[0]):
    temp = []
    for j in range(data.shape[1]):
        if data.values[i, j] == 1:
            temp.append(data.columns[j])
    records.append(temp)

association_rules = apriori(records, min_support=0.3, min_confidence=0.7)
association_rules = list(association_rules)

for i in association_rules:
    print(i)
