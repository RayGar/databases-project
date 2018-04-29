# Import the necessary libraries
import matplotlib.pyplot as plt
import pandas as pd

# Seaborn for plotting and styling
import seaborn as sns

# Initialize Figure and Axes object
fig, ax = plt.subplots()

# Load in data
tips = pd.read_csv("people.csv")

# Count Plot (a.k.a. Bar Plot)
#sns.countplot(x='runtimeMinutes', data=tips, order=tips.primaryProfession.value_counts().iloc[:10].index) 


# Recommended way
sns.distplot(tips.runtimeMinutes, df=tips)


# Show the plot
plt.show()