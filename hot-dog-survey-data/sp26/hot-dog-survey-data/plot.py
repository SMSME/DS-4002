import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

filename = r"/Users/jam/Desktop/ds/DS-4002/hot-dog-survey-data/sp26/hot-dog-survey-data/Hotdog Survey (Responses) - Form Responses 1.csv"
data = pd.read_csv(filename)


# Plot the yes vs no
sns.set(style="whitegrid")
ax = sns.countplot(x='Is a Hotdog a Sandwich?', data=data)
plt.show() 

