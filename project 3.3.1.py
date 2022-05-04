import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
europe = ["United States", "England", "Russia", "Germany", "Japan", "Saudi Arabia", "India", "China"]
df = pd.read_csv("population-by-country.csv", header=0)
unique_countries = df['Entity'].unique()
for c in unique_countries:
  if c in europe:
    years = df[df['Entity'] == c]['Year']
    total_population =(df[df['Entity'] == c]['Total_population'])

    plt.plot(years, total_population, label=c, linestyle = ":")
  plt.ylabel('Population by Country vs Time')
plt.xlabel('Year')
plt.title('Historical Populations by Country')
plt.legend()
plt.show()