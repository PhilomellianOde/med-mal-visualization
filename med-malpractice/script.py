import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

print(np.random.randint(1,9))

# Read in Medical Malpractice CSV data
df = pd.read_csv("data/raw-data/medicalmalpractice.csv")


print(df.head())

print(df.head())

print(df['Insurance'].value_counts())



# Let's take a look at how claims are distributed. We'll take a look at the shape of the distribution.
sns.histplot(data=df, x = "Amount", kde = True)
plt.show()