import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv("advertising.csv")


def correlation(x, y):
    N = len(x)
    numerator = N*np.sum(x*y) - np.sum(x)*np.sum(y)
    denominator = np.sqrt(N*np.sum(x**2) - np.sum(x)**2) * \
        np.sqrt(N*np.sum(y**2) - np.sum(y)**2)
    return np.round(numerator/denominator, 2)


# Question 5
x = data['TV']
y = data['Radio']
corr_xy = correlation(x, y)
print(f"Correlation between TV and Sales: {round(corr_xy, 2)}")


# Question 6
features = ['TV', 'Radio', 'Newspaper']
for feature_1 in features:
    for feature_2 in features:
        correlation_value = correlation(data[feature_1], data[feature_2])
        print(
            f"Correlation between {feature_1} and {feature_2}: {round(correlation_value, 2)}")


# Question 7
x = data['Radio']
y = data['Newspaper']

result = np.corrcoef(x, y)
print(result)
print(data.corr())


# Question 9
plt.figure(figsize=(10, 8))
data_corr = data.corr()
sns.heatmap(data_corr, annot=True, fmt=".2f", linewidth=.5)
plt.show()
