import pandas as pd

folder_path = "./AIO-Exercise/Module_2/Week_1/assets/"
data_path = folder_path + "advertising.csv"
df = pd.read_csv(data_path)
data = df.to_numpy()

# cau 15
print("\nCau 15:")
print(f"Max: {df['Sales'].max()} - Index: {df['Sales'].argmax()}")

# cau 16
print("\nCau 16:")
print(df['TV'].mean())

# cau 17
print("\nCau 17:")
records = df['Sales'] >= 20
print(records.sum())

# cau 18
print("\nCau 18:")
df1 = df[df['Sales'] >= 15]
print(df1['Radio'].mean())

# cau 19
print("\nCau 19:")
df2 = df[df['Newspaper'] > df['Newspaper'].mean()]
print(df2['Sales'].sum())

# cau 20
print("\nCau 20:")
A = df['Sales'].mean()
scores = pd.Series(["" for _ in range(len(df['Sales']))])
scores[df['Sales'] > A] = 'Good'
scores[df['Sales'] == A] = 'Average'
scores[df['Sales'] < A] = 'Bad'
scores = list(scores)
print(scores[7:10])

# cau 21
print("\nCau 21:")
sales = df['Sales']
mean_val = sales.mean()
A1 = abs(sales - mean_val).idxmin()
scores1 = pd.Series(["" for _ in range(len(sales))])
scores1[sales > sales[A1]] = 'Good'
scores1[sales == sales[A1]] = 'Average'
scores1[sales < sales[A1]] = 'Bad'
scores1 = list(scores1)
print(scores1[7:10])