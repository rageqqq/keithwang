import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Interpolating Function
def P3(x):
    part1 = -220.8432 * (x-2005) * (x-2010) * (x-2015)
    part2 = 850.892 * (x-2000) * (x-2010) * (x-2015)
    part3 = -1307.9204 * (x-2000) * (x-2005) * (x-2015)
    part4 = 564.592 * (x-2000) * (x-2005) * (x-2010)

    return part1 + part2 + part3 + part4


# Read file and Calculate estimated GDP
GDP = pd.read_csv("GDP.csv", header=None)
GDP.rename(columns={0:'Year', 1:'True_GDP'}, inplace=True)
GDP['Estimated_GDP'] = GDP['Year'].map(lambda x: P3(x))

## Plot Graph
# Format plot size and font size
plt.figure(figsize=(20, 16))
plt.rcParams.update({'font.size': 20})
plt.gca().set_title('True VS Estimated GDP (1999—2019)')

# Plot
plt.plot('Year', 'True_GDP', data=GDP, marker='o')
plt.plot('Year', 'Estimated_GDP', data=GDP, marker='o')

# Format x-axis interval
plt.xticks(np.arange(1999, 2020, 5))

# Not important
plt.legend()
plt.savefig("true_vs_estimated_GDP.jpeg")
