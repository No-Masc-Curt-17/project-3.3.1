import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
big_countries = ["United States", "England", "Russia", "Germany", "Japan", "Saudi Arabia", "India", "China"]
df = pd.read_csv("population-by-country.csv", header=0)
unique_countries = df['Entity'].unique()
#average
total = 0
country_count = 0
for i in range(len(df(['Entity']))):
  if df['Entity'][i] in big_countries:
    total += df['Total_Population'][i]
    country_count +=1
average = total/country_count
print("average:", average)

for c in unique_countries:
  if c in big_countries:
    years = df[df['Entity'] == c]['Year']
    total_population =(df[df['Entity'] == c]['Total_population'])

    plt.plot(years, total_population, label=c, linestyle = ":")
  plt.ylabel('Population by Country vs Time')
plt.xlabel('Year')
plt.title('Historical Populations by Country')
plt.legend()
plt.show()