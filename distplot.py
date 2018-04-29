# Import the necessary libraries
import matplotlib.pyplot as plt
import pandas as pd

# Seaborn for plotting and styling
import seaborn as sns

# Initialize Figure and Axes object
fig, ax = plt.subplots()

# Load in data
tips = pd.read_csv("people.csv")

# Create the graph
sns.distplot(tips.runtimeMinutes, )
plt.xlim(0, 300)

# Show the plot
plt.show()