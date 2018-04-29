# Import the necessary libraries
import matplotlib.pyplot as plt
import pandas as pd

# Seaborn for plotting and styling
import seaborn as sns

# Initialize Figure and Axes object
fig, ax = plt.subplots()

# Load in data
tips = pd.read_csv("fixed_title_akas.csv")

# Count Plot (a.k.a. Bar Plot)
sns.countplot(x='region', data=tips, order=tips.region.value_counts().iloc[:15].index)

# Show the plot
plt.show()