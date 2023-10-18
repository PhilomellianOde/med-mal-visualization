import numpy as np
import pandas as pd
import seaborn as sn

print(np.random.randint(1,9))

# Read in Medical Malpractice CSV data
med_data = pd.read_csv("data/raw-data/medicalmalpractice.csv")


print(med_data.head())